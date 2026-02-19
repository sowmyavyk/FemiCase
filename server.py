from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
import asyncio

from src.bot import PersonalReplyBot
from src.integrations.webhooks import WebhookSender

app = FastAPI(title="Personal Reply Bot API", version="2.0")
bot = PersonalReplyBot()
webhook_sender = WebhookSender()


class MessageRequest(BaseModel):
    message: str
    user_id: Optional[str] = "default"


class TrainingRequest(BaseModel):
    input_text: str
    reply: str
    language: Optional[str] = "en"


class PersonalityRequest(BaseModel):
    personality: str


class CorrectionRequest(BaseModel):
    query: str
    original: str
    corrected: str
    user_id: Optional[str] = "default"


@app.get("/")
async def root():
    return {
        "status": "running",
        "bot": "Personal Reply Bot v2.0",
        "endpoints": {
            "/chat": "POST - Send a message",
            "/train": "POST - Add training example",
            "/personality": "POST - Change personality",
            "/correct": "POST - Correct a reply",
            "/stats": "GET - Get bot stats",
            "/memory": "POST - Add long-term memory",
            "/clear": "POST - Clear conversation"
        }
    }


@app.post("/chat")
async def chat(request: MessageRequest):
    result = bot.get_reply(request.message, request.user_id)
    return {
        "reply": result["reply"],
        "user_id": request.user_id,
        "stats": result["stats"]
    }


@app.post("/train")
async def train(request: TrainingRequest):
    bot.train(request.input_text, request.reply, request.language)
    return {"status": "success", "message": "Training example added"}


@app.post("/personality")
async def change_personality(request: PersonalityRequest):
    success = bot.set_personality(request.personality)
    if success:
        return {"status": "success", "personality": request.personality}
    raise HTTPException(status_code=400, detail="Invalid personality")


@app.post("/correct")
async def correct(request: CorrectionRequest):
    result = bot.correct(request.query, request.original, request.corrected, request.user_id)
    return {"status": "success", "message": result}


@app.get("/stats")
async def stats():
    return bot.get_stats()


@app.post("/memory")
async def add_memory(user_id: str, fact: str):
    bot.add_memory(user_id, fact)
    return {"status": "success", "message": f"Remembered: {fact}"}


@app.post("/clear")
async def clear_conversation(user_id: str = "default"):
    bot.clear_conversation(user_id)
    return {"status": "success", "message": "Conversation cleared"}


@app.get("/personalities")
async def list_personalities():
    return bot.list_personalities()


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        user_id = str(chat_id)
        
        if text:
            reply = bot.get_reply(text, user_id)["reply"]
            
            webhook_sender.send_telegram(f"🤖 {reply}", chat_id)
    
    return {"ok": True}


@app.post("/discord/webhook")
async def discord_webhook(request: Request):
    data = await request.json()
    
    if data.get("type") == 1:
        return {"type": 1}
    
    if "content" in data:
        user_message = data["content"]
        user_id = str(data.get("author", {}).get("id", "discord"))
        
        reply = bot.get_reply(user_message, user_id)["reply"]
        
        webhook_sender.send_discord(f"🤖 {reply}")
    
    return {"ok": True}


def run_server(host: str = "0.0.0.0", port: int = 8000):
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║           PERSONAL REPLY BOT - API SERVER                  ║
╚═══════════════════════════════════════════════════════════╝

🌐 API:      http://localhost:{port}
📖 Docs:     http://localhost:{port}/docs
📡 Webhooks: http://localhost:{port}/telegram/webhook
              http://localhost:{port}/discord/webhook

Ready to receive messages!
""")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
