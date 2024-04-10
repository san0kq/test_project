from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemDTO:
    key: str
    value: Optional[str] = None
