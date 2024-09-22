import json
from dataclasses import dataclass
from typing import Any

from .raceTable import RaceTable


@dataclass
class MRData:
    xmlns: str
    series: str
    url: str
    limit: str
    offset: str
    total: str
    RaceTable: RaceTable

    @staticmethod
    def from_dict(obj: Any) -> 'MRData':
        _xmlns = str(obj.get("xmlns"))
        _series = str(obj.get("series"))
        _url = str(obj.get("url"))
        _limit = str(obj.get("limit"))
        _offset = str(obj.get("offset"))
        _total = str(obj.get("total"))
        _RaceTable = RaceTable.from_dict(obj.get("RaceTable"))
        return MRData(_xmlns, _series, _url, _limit, _offset, _total, _RaceTable)
