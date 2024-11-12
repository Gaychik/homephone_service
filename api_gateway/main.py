from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

# Адреса сервисов
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
CALL_SERVICE_URL = os.getenv("CALL_SERVICE_URL")

# Модель для данных пользователя
class User(BaseModel):
    name: str
    phone: str

@app.get("/hello/{name}")
def hello(name : str):
    return f"You are have reached the API Gateway,{name}!"

# Маршруты API Gateway
@app.post("/users/")
async def create_user(user: User):
    """Создать нового пользователя через User Service"""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/users/", json=user.model_dump_json())
        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Получить информацию о пользователе по ID через User Service"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


@app.post("/calls/")
async def make_call(request: Request):
    """Инициировать звонок через Call Service"""
    call_data = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{CALL_SERVICE_URL}/calls/", json=call_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/calls/history/")
async def get_call_history():
    """Получить историю звонков через Call Service"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CALL_SERVICE_URL}/calls/history/")
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
