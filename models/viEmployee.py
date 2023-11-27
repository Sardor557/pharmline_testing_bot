from dataclasses import dataclass


@dataclass
class ViEmployee:
    id: int
    telegramId: int
    token: str
    lang: str
