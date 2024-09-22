from typing import Any
from dataclasses import dataclass
from .location import Location


@dataclass
class Circuit:
    circuitId: str
    url: str
    circuitName: str
    Location: Location

    @staticmethod
    def from_dict(obj: Any) -> 'Circuit':
        _circuitId = str(obj.get("circuitId"))
        _url = str(obj.get("url"))
        _circuitName = str(obj.get("circuitName"))
        _Location = Location.from_dict(obj.get("Location"))
        return Circuit(_circuitId, _url, _circuitName, _Location)

