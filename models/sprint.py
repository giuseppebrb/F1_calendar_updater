from dataclasses import dataclass
from typing import Any


@dataclass
class Sprint:
    date: str
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'Sprint':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return Sprint(_date, _time)
