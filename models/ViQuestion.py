from dataclasses import dataclass
from typing import List

from models.ViOption import ViOption


@dataclass
class ViQuestion:
    id: int
    context: str
    isOpen: bool
    options: List[ViOption]
