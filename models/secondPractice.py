from dataclasses import dataclass
from typing import Any
from .timeTable import TimeTable


@dataclass
class SecondPractice(TimeTable):

    def __init__(self, date, time):
        super().__init__(date, time)

    @staticmethod
    def from_dict(obj: Any) -> 'SecondPractice':
        if not obj:
            return SecondPractice(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return SecondPractice(_date, _time)
