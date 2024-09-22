from dataclasses import dataclass
from typing import Any


@dataclass
class FirstPractice:
    date: str
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'FirstPractice':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return FirstPractice(_date, _time)
