import aiohttp
import json

from models.Answer import Answer
from models.AnswerBasic import AnswerBasic
from models.AuthorizationModel import AuthorizationModel
from models.ViDrug import ViDrug
from models.ViOption import ViOption
from models.ViQuestion import ViQuestion
from models.viAnswer import ViAnswer
from models.viEmployee import ViEmployee
from utils.global_vars import SERVER_URL


def set_header(token) -> dict:
    return {
            'accept': 'text/plain',
            'Authorization': f'Bearer {token}'
        }


async def is_user_registered_async(chat_id: int, token) -> bool:
    headers = set_header(token)
    async with aiohttp.ClientSession() as session:
        res = await session.get(SERVER_URL + "Employee/" + str(chat_id), headers=headers)
        try:
            if res.status == 200:
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
        res = await client.post(SERVER_URL + "Employee/login", data=json.dumps(model.__dict__), headers=headers)
        try:
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = ViEmployee(**answer.data)

            return answer
        finally:
            res.close()


async def get_drugs_async(token) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        res = await client.get(SERVER_URL + "Dico/drugs?status=1", headers=headers)
        try:
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
        res = await client.get(SERVER_URL + f"Dico/drug/{drug_name}", headers=headers)
        try:
            js = await res.json()
            answer = Answer(**js)
            return answer
        finally:
            res.close()


async def get_drug_question_async(token, drug_id, over_id) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        res = await client.get(SERVER_URL + f"Question/by_drug/{drug_id}/{over_id}", headers=headers)
        try:
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = ViQuestion(**answer.data)
                answer.data.options = [ViOption(**item) for item in answer.data.options]
            return answer
        finally:
            res.close()


async def get_current_question_async(token, question_id) -> Answer:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        res = await client.get(SERVER_URL + f"Question/current/{question_id}", headers=headers)
        try:
            js = await res.json()
            answer = Answer(**js)
            if answer.data is not None:
                answer.data = ViQuestion(**answer.data)
                answer.data.options = [ViOption(**item) for item in answer.data.options]
            return answer
        finally:
            res.close()


async def add_answer_async(token, answer: ViAnswer) -> AnswerBasic:
    async with aiohttp.ClientSession() as client:
        headers = set_header(token)
        headers['Content-Type'] = 'application/json-patch+json'
        res = await client.post(SERVER_URL + 'Answer/add', data=json.dumps(answer.__dict__), headers=headers)
        try:
            js = await res.json()
            return AnswerBasic(**js)
        finally:
            res.close()
