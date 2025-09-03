from fastapi import FastAPI, Request, Response
import requests

app = FastAPI()

# Псевдо-endpoint проксі
@app.get("/api/proxy/")
async def proxy(url: str):
    # Робимо запит до стороннього сервера
    r = requests.get(url, headers={"ngrok-skip-browser-warning": "true"}, stream=True)
    return Response(content=r.content, media_type=r.headers.get("content-type"))
