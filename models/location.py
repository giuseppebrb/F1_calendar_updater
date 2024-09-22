from dataclasses import dataclass
from typing import Any


@dataclass
class Location:
    lat: str
    long: str
    locality: str
    country: str

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        _lat = str(obj.get("lat"))
        _long = str(obj.get("long"))
        _locality = str(obj.get("locality"))
        _country = str(obj.get("country"))
        return Location(_lat, _long, _locality, _country)

