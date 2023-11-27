import json
from dataclasses import dataclass


@dataclass
class AnswerBasic:
    isSuccess: bool
    message: str

    def __init__(self, js: str):
        self.__dict__ = json.loads(js)
