from dataclasses import dataclass
from datetime import datetime


@dataclass
class ViDrug:
    id: int
    name: str
    status: int
    createUser: int
    createDate: datetime
    updateUser: int
    updateDate: datetime
