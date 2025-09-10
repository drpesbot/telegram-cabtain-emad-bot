import os

from fastapi import FastAPI, Request

from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, CommandHandler

TOKEN = os.environ.get("TOKEN")  # التوكن هيتحدد في Vercel

app = FastAPI()

async def start(update: Update, context):
    await update.message.reply_text(
        "اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد \nهذا هو الرابط تفضل بالضغط عليه ⬇️⬇️\nhttps://t.me/pes224"
    )

async def echo(update: Update, context):
    await update.message.reply_text(
        "اضغط على الرابط الذى بالاسفل للوصول إلى ستور كابتن عماد \nهذا هو الرابط تفضل بالضغط عليه ⬇️⬇️\nhttps://t.me/pes224"
    )

@app.post("/webhook")
async def webhook(request: Request):
    # Get the JSON data from the request body
    webhook_data = await request.json()

    # Initialize the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Process the update
    update = Update.de_json(webhook_data, application.bot)
    await application.process_update(update)

    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}

