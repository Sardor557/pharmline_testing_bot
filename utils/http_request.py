import aiohttp
import json

from models.Answer import Answer
from models.AuthorizationModel import AuthorizationModel
from models.viEmployee import ViEmployee
from utils.global_vars import SERVER_URL


async def is_user_registered(chat_id: int) -> bool:
    headers = {
        'accept': 'text/plain'
    }
    async with aiohttp.ClientSession() as session:
        res = await session.get(SERVER_URL + "Employee/" + str(chat_id), headers=headers)
        if res.status == 200:
            print(res)
            data = await res.read()
            print(data)
            js = json.loads(data)
            print(js)
            return True

    return False


async def authorize(model: AuthorizationModel) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json-patch+json'
        }
        res = await client.post(SERVER_URL + "Employee/login", data=json.dumps(model.__dict__), headers=headers)
        js = await res.json()
        answer = Answer(**js)
        answer.data = ViEmployee(**answer.data)

        return answer
