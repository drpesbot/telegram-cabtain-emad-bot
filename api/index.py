import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, CommandHandler

TOKEN = os.environ.get("TOKEN")  # التوكن هيتحدد في Vercel

app = FastAPI()

class TelegramWebhook(BaseModel):
    update_id: int
    message: Optional[dict]

async def start(update, context):
    await update.message.reply_text(
        "اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد \nهذا هو الرابط تفضل بالضغط عليه ⬇️⬇️\nhttps://t.me/pes224"
    )

async def echo(update, context):
    await update.message.reply_text(
        "اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد \nهذا هو الرابط تفضل بالضغط عليه ⬇️⬇️\nhttps://t.me/pes224"
    )

@app.post("/webhook")
async def webhook(webhook_data: dict):
    bot = Bot(token=TOKEN)
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    update = Update.de_json(webhook_data, bot)
    await application.process_update(update)
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}

