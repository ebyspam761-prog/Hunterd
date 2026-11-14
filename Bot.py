import os
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Hunterd 🕵️\n"
        "Я отслеживаю публичные раздачи DCard на Donatov.\n"
        "Команда /scan — начать поиск."
    )

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Начинаю проверку Donatov...")

    try:
        response = requests.get(
            "https://donatov.net/",
            timeout=15,
            headers={"User-Agent": "Hunterd/1.0"}
        )
        if response.status_code == 200:
            await update.message.reply_text(
                "Сайт доступен! Но поиск кодов ещё нужно настроить."
            )
        else:
            await update.message.reply_text(
                f"Сайт ответил с кодом {response.status_code}."
            )
    except requests.RequestException:
        await update.message.reply_text("Не удалось подключиться к сайту.")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
