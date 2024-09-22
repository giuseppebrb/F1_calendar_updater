from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class SecondPractice:
    date: Optional[str]
    time: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> 'SecondPractice':
        if not obj:
            return SecondPractice(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return SecondPractice(_date, _time)
