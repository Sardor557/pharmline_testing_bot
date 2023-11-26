from dataclasses import dataclass


@dataclass
class AuthorizationModel:
    phone: str
    password: str
    telegramId: int
    lang: str
