import json
from dataclasses import dataclass


@dataclass
class AuthorizationModel:
    phone: str
    password: str
    telegramId: int
    lang: str

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
