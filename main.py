
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]
GROUP_ID = os.environ.get("GROUP_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ISIUZ SECURITY BOT ishga tayyor! ✅"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot faol ishlayapti. 🟢")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not GROUP_ID:
        await update.message.reply_text("Guruh ID hali sozlanmagan.")
        return

    await context.bot.send_message(
        chat_id=GROUP_ID,
        text="ISIUZ SECURITY BOT: test xabari! ✅"
    )
    await update.message.reply_text("Test xabari yuborildi!")

async def post_init(app):
    if GROUP_ID:
        await app.bot.send_message(
            chat_id=GROUP_ID,
            text="ISIUZ SECURITY BOT ishga tushdi! 🟢"
        )

app = (
    Application.builder()
    .token(BOT_TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("test", test))

if __name__ == "__main__":
    app.run_polling()
