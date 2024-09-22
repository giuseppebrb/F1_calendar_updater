from dataclasses import dataclass
from typing import List, Any
from .race import Race


@dataclass
class RaceTable:
    season: str
    Races: List[Race]

    @staticmethod
    def from_dict(obj: Any) -> 'RaceTable':
        _season = str(obj.get("season"))
        _Races = [Race.from_dict(y) for y in obj.get("Races")]
        return RaceTable(_season, _Races)
