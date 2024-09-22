# Formula 1 Calendar Updater
A Python script that fetches the Formula 1 schedule from jolpi.ca/ergast API and adds the races to your Google Calendar.

## Features

* Fetches the current Formula 1 schedule from jolpi.ca/ergast API
* Adds each race to your Google Calendar as a separate event
* Sets reminders for each event (24 hours and 1 hour before the race)

## Requirements

* Python 3.x
* Google API Client Library for Python
* `credentials.json` file with your Google Calendar API credentials
* `token.json` file (created automatically when running the script for the first time)

## Usage

1. Create a new file named `credentials.json` and add your Google Calendar API credentials.
2. Run the script using `python main.py`.
3. The script will fetch the current Formula 1 schedule and add each race to your Google Calendar.

## Notes

* This script uses the `jolpi.ca/ergast` API to fetch the Formula 1 schedule. Please note that this API may change or become unavailable at any time.
* This script uses the Google Calendar API to add events to your calendar. You need to have the `https://www.googleapis.com/auth/calendar` scope enabled in your Google Cloud Console project.
* The script will create a new `token.json` file in the current directory to store your Google Calendar API credentials. This file will be created automatically when running the script for the first time.

## License

This script is licensed under the MIT License. See `LICENSE` for details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Credits

* [jolpi.ca/ergast API](https://api.jolpi.ca/ergast/) for providing the Formula 1 schedule data
* [Google Calendar API](https://developers.google.com/calendar) for providing the calendar events API
* [Google API Client Library for Python](https://github.com/googleapis/google-api-python-client) for providing the Python client library for the Google Calendar API