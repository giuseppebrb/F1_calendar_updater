from dataclasses import dataclass
from typing import Any
from .circuit import Circuit
from .firstPractice import FirstPractice
from .secondPractice import SecondPractice
from .thirdPractice import ThirdPractice
from .qualifying import Qualifying
from .sprint import Sprint

@dataclass
class Race:
    season: str
    round: str
    url: str
    raceName: str
    Circuit: Circuit
    date: str
    time: str
    FirstPractice: FirstPractice
    SecondPractice: SecondPractice
    ThirdPractice: ThirdPractice
    Qualifying: Qualifying
    Sprint: Sprint

    @staticmethod
    def from_dict(obj: Any) -> 'Race':
        _season = str(obj.get("season"))
        _round = str(obj.get("round"))
        _url = str(obj.get("url"))
        _raceName = str(obj.get("raceName"))
        _Circuit = Circuit.from_dict(obj.get("Circuit"))
        _date = str(obj.get("date"))
        _time = str(obj.get("time"))
        _FirstPractice = FirstPractice.from_dict(obj.get("FirstPractice"))
        _SecondPractice = SecondPractice.from_dict(obj.get("SecondPractice"))
        _ThirdPractice = ThirdPractice.from_dict(obj.get("ThirdPractice"))
        _Qualifying = Qualifying.from_dict(obj.get("Qualifying"))
        _Sprint = Sprint.from_dict(obj.get("Sprint"))
        return Race(_season, _round, _url, _raceName, _Circuit, _date, _time, _FirstPractice, _SecondPractice, _ThirdPractice, _Qualifying, _Sprint)
