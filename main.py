import datetime
import os.path
import sys

import pytz
import requests
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from models import RaceTable, Root, Race, TimeTable, FirstPractice, SecondPractice, ThirdPractice, Qualifying, Sprint

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        race_table = fetch_formula_one_schedule()
        for race in race_table.Races:
            if race.FirstPractice.date:
                add_calendar_event(service, race, race.FirstPractice)
            if race.SecondPractice.date:
                add_calendar_event(service, race, race.SecondPractice)
            if race.ThirdPractice.date:
                add_calendar_event(service, race, race.ThirdPractice)
            if race.Qualifying.date:
                add_calendar_event(service, race, race.Qualifying)
            if race.Sprint.date:
                add_calendar_event(service, race, race.Sprint)
            add_calendar_event(service, race, TimeTable(date=race.date, time=race.time), True)

    except HttpError as error:
        print(f"An error occurred: {error}")


def fetch_formula_one_schedule(season=datetime.datetime.now().year) -> RaceTable:
    """
    Fetch the F1 schedule from jolpi.ca/ergast API
    """
    request = requests.get(f'https://api.jolpi.ca/ergast/f1/{season}.json')
    json_response = json.loads(request.text)
    root = Root.from_dict(json_response)
    return root.MRData.RaceTable


def add_calendar_event(service, race: Race, timetable: TimeTable, early_reminder=False):
    """
    Add a race event to the calendar
    :param service: Configured service that will be used to add the race event
    :param race: Race info
    :param timetable: Schedule of this event
    :param early_reminder: If True set an early reminder starting from the day before
    :return:
    """
    event = {
        'summary': assign_event_name(race.raceName, timetable),
        'start': {
            'dateTime': parse_date(timetable.date, timetable.time).isoformat(),
        },
        'end': {
            'dateTime': (parse_date(timetable.date, timetable.time) + datetime.timedelta(hours=1, minutes=30)).isoformat(),
        },
        'reminders': {
            'useDefault': True,
        },
    }

    if early_reminder:
        event['reminders'] = {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 60},
            ],
        }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Race added: %s' % (event.get('htmlLink')))


def parse_date(date, time) -> datetime.datetime:
    """
    Parse a date to standard datetime object in UTC timezone
    :param date: Origin date
    :param time: Origin time
    :return:
    """
    date_str = f'{date} {time}'
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%SZ")
        date_obj = pytz.UTC.localize(date_obj)
        return date_obj
    except ValueError as err:
        print(err, f'invalid date {date}')
        sys.exit(1)


def assign_event_name(race_name: str, event: TimeTable) -> str:
    """
    Return a title based on the event type
    :param race_name: Grand Prix name
    :param event: Object representing the event (First Practice, Second Practice, Third Practice, Qualifying, Sprint)
    :return:
    """
    if isinstance(event, FirstPractice):
        return f'1️⃣st Practice @ {race_name}'
    elif isinstance(event, SecondPractice):
        return f'2️⃣nd Practice @ {race_name}'
    elif isinstance(event, ThirdPractice):
        return f'3️⃣ Practice @ {race_name}'
    elif isinstance(event, Qualifying):
        return f'⏱️ Qualifying @ {race_name}'
    elif isinstance(event, Sprint):
        return f'🏎️ Sprint Race @ {race_name}'
    else:
        return '🏁 ' + race_name


if __name__ == "__main__":
    main()
