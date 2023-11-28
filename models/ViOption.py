from dataclasses import dataclass


@dataclass
class ViOption:
    id: int
    questionId: int
    variant: str
