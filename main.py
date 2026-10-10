from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random

app = FastAPI(title="VibeBoard")


class GreetingInput(BaseModel):
    name: str
    mood: str


MOOD_MESSAGES = {
    "happy": "You are radiating good energy today.",
    "focused": "Stay sharp and keep the momentum rolling.",
    "creative": "Your ideas are about to get interesting.",
    "chill": "A calm rhythm is exactly what this moment needs.",
    "adventurous": "The next move could be your best one yet.",
}


@app.get("/")
def read_index() -> FileResponse:
    return FileResponse("static/index.html")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "message": "FastAPI backend is live"}


@app.post("/api/greeting")
def make_greeting(payload: GreetingInput) -> dict[str, str]:
    name = (payload.name or "friend").strip() or "friend"
    mood = (payload.mood or "happy").strip().lower() or "happy"
    message = MOOD_MESSAGES.get(mood, MOOD_MESSAGES["happy"])
    emoji = {
        "happy": "✨",
        "focused": "🎯",
        "creative": "🎨",
        "chill": "🌙",
        "adventurous": "🚀",
    }.get(mood, "✨")

    return {
        "message": f"Hello, {name}! {message} {emoji}",
        "quote": random.choice([
            "Small steps still move you forward.",
            "Your next idea could change everything.",
            "Progress feels better when you enjoy the process.",
            "A little momentum is all you need to begin.",
        ]),
    }


app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
