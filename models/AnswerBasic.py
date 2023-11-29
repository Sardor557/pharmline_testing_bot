import json
from dataclasses import dataclass


@dataclass
class AnswerBasic:
    isSuccess: bool
    message: str
