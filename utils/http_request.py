import aiohttp
import json

from models.Answer import Answer
from models.AuthorizationModel import AuthorizationModel
from models.ViDrug import ViDrug
from models.ViOption import ViOption
from models.ViQuestion import ViQuestion
from models.viEmployee import ViEmployee
from utils.global_vars import SERVER_URL


async def is_user_registered_async(chat_id: int) -> bool:
    headers = {
        'accept': 'text/plain'
    }
    async with aiohttp.ClientSession() as session:
        try:
            res = await session.get(SERVER_URL + "Employee/" + str(chat_id), headers=headers)
            if res.status == 200:
                print(res)
                data = await res.read()
                print(data)
                js = json.loads(data)
                print(js)
                return True
        finally:
            res.close()
    return False


async def authorize_async(model: AuthorizationModel) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json-patch+json'
        }
        try:
            res = await client.post(SERVER_URL + "Employee/login", data=json.dumps(model.__dict__), headers=headers)
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = ViEmployee(**answer.data)

            return answer
        finally:
            res.close()


def set_header(token) -> dict:
    return {
            'accept': 'text/plain',
            'Authorization': f'Bearer {token}'
        }


async def get_drugs_async(token) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        try:
            res = await client.get(SERVER_URL + "Dico/drugs?status=1", headers=headers)
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = [ViDrug(**item) for item in answer.data]

            return answer
        finally:
            res.close()


async def get_drug_id_async(token, drug_name) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        try:
            res = await client.get(SERVER_URL + f"Dico/drug/{drug_name}", headers=headers)
            js = await res.json()
            answer = Answer(**js)
            return answer
        finally:
            res.close()


async def get_drug_question_async(token, drug_id, over_id) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        try:
            res = await client.get(SERVER_URL + f"Question/by_drug/{drug_id}/{over_id}", headers=headers)
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = ViQuestion(**answer.data)
                answer.data.options = [ViOption(**item) for item in answer.data.options]
            return answer
        finally:
            res.close()
