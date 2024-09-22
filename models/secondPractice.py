from dataclasses import dataclass
from typing import Any


@dataclass
class SecondPractice:
    date: str
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'SecondPractice':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return SecondPractice(_date, _time)
