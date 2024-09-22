from dataclasses import dataclass
from typing import Any


@dataclass
class Qualifying:
    date: str
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'Qualifying':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return Qualifying(_date, _time)
