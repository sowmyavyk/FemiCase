import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes
from src.bot import PersonalReplyBot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

if not BOT_TOKEN:
    print("❌ TELEGRAM_BOT_TOKEN not set in .env")
    print("Get it from @BotFather on Telegram")
    exit(1)

bot = PersonalReplyBot()
print("🤖 Personal Reply Bot initializing...")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey! I'm your personal reply bot 🤖\n"
        "I'll reply to your messages in YOUR style!\n\n"
        "Just chat with me and I'll learn from you."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    message_text = update.message.text
    
    reply = bot.get_reply(message_text, user_id)["reply"]
    
    await update.message.reply_text(reply)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(None, handle_message))
    
    app.add_error_handler(error_handler)
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║           PERSONAL REPLY BOT - TELEGRAM                   ║
╚═══════════════════════════════════════════════════════════╝

🤖 Bot is running! Start chatting on Telegram.

Commands:
/start - Start the bot
""")
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
