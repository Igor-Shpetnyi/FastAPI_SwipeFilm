from fastapi import FastAPI, Request, Response
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "http://localhost:5173",
    # "https://igor-shpetnyi.github.io",
    "*",  # можна для тесту дозволити всім, але небезпечно в продакшені
]

app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
NGROK_URL = "https://teaching-annually-asp.ngrok-free.app"

# Псевдо-endpoint проксі
@app.get("/proxy/")
async def proxy(data: str):
    # Робимо запит до стороннього сервера
    r = requests.get(f"{NGROK_URL}{data}", headers={"ngrok-skip-browser-warning": "true"}, stream=True)
    return Response(content=r.content, media_type=r.headers.get("content-type"))
