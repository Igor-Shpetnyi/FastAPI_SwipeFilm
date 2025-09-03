from fastapi import FastAPI, Request, Response
import requests

app = FastAPI()

NGROK_URL = "https://teaching-annually-asp.ngrok-free.app"

# Псевдо-endpoint проксі
@app.get("/proxy/")
async def proxy(data: str):
    # Робимо запит до стороннього сервера
    r = requests.get(f"{NGROK_URL}{data}", headers={"ngrok-skip-browser-warning": "true"}, stream=True)
    return Response(content=r.content, media_type=r.headers.get("content-type"))
