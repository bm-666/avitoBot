import aiohttp
import asyncio
import aiofiles

from typing import Any


#URL_TOKEN = 'https://api.avito.ru/token/'
#CLIENT_ID = Ваш client_id полученный при регистрации приложения в Avito
#CLIENT_SECRET = Ваш client_secret полученный при регистрации приложения в Avito

headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }

body = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

async def write_read_file(filename: str, mode: str, data: Any = None):
    # Запись/чтение файла
    async with aiofiles.open(filename, mode=mode) as file:
        if data is not None:
            await file.write(f'{data}'.encode())
            return "Ok"
        else:
            print(await file.read())


async def get_access_token(url_token: str, data: dict, headers: dict) -> dict:
    #Запрос access_token параметры:
    # - Url default 'https://api.avito.ru/token/'
    # - Data dict params 'grant_type': 'client_credentials', 'client_id':<CLIENT_ID>, 'client_secret': <CLIENT_SECRET>
    # - Headers dict {'content-type': 'application/x-www-form-urlencoded'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url_token, data=data, headers=headers) as resp:
            return await resp.json()


async def get_accaunt_info(user_id: int):
    url = f'https://api.avito.ru/core/v1/accounts/{user_id}/'
    headers = {'Authorization': 'Bearer <your_token>'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            print(await resp.text())

