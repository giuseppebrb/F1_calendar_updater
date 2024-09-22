from dataclasses import dataclass
from typing import Any


@dataclass
class ThirdPractice:
    date: str
    time: str

    @staticmethod
    def from_dict(obj: Any) -> 'ThirdPractice':
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return ThirdPractice(_date, _time)