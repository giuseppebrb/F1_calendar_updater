from dataclasses import dataclass
from typing import Any
from .timeTable import TimeTable


@dataclass
class ThirdPractice(TimeTable):

    def __init__(self, date, time):
        super().__init__(date, time)

    @staticmethod
    def from_dict(obj: Any) -> 'ThirdPractice':
        if not obj:
            return ThirdPractice(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return ThirdPractice(_date, _time)