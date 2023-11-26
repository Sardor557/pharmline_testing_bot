import json
import aiohttp

from models.AuthorizationModel import AuthorizationModel
from utils.global_vars import SERVER_URL



headers = {
        'accept: text/plain'
    }

async def is_user_registered(chat_id: int) -> bool:
    async with aiohttp.ClientSession() as session:
        res = await session.get(SERVER_URL + chat_id, headers=headers)
        if res.status == 200:
            return True

    return False


async def authorize(model: AuthorizationModel) -> str:
    async with aiohttp.ClientSession() as client:
        res = await client.post(SERVER_URL + "login", data=json.dump(model.__dict__), headers=headers)