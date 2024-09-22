from dataclasses import dataclass
from typing import Any
from .timeTable import TimeTable


@dataclass
class Qualifying(TimeTable):
    def __init__(self, date, time):
        super().__init__(date, time)

    @staticmethod
    def from_dict(obj: Any) -> 'Qualifying':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return Qualifying(_date, _time)
