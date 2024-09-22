from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Sprint:
    date: Optional[str] = None
    time: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sprint':
        if not obj:
            return Sprint(None, None)
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        return Sprint(_date, _time)
