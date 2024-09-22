from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ThirdPractice:
    date: Optional[str]
    time: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> 'ThirdPractice':
        if not obj:
            return ThirdPractice(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return ThirdPractice(_date, _time)