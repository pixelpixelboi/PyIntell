from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(msg: Message):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": msg.prompt}
    )
    data = r.json()
    return {"response": data.get("response", "")}
