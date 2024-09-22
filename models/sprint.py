from dataclasses import dataclass
from typing import Any, Optional
from .timeTable import TimeTable

@dataclass
class Sprint(TimeTable):
    def __init__(self, date, time):
        super().__init__(date, time)

    @staticmethod
    def from_dict(obj: Any) -> 'Sprint':
        if not obj:
            return Sprint(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return Sprint(_date, _time)
