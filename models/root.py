from dataclasses import dataclass
from typing import Any
from .mRData import MRData


@dataclass
class Root:
    MRData: MRData

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _MRData = MRData.from_dict(obj.get("MRData"))
        return Root(_MRData)
