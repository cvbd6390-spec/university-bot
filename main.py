from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "Done! Congratulations on your new bot. You will find it at t.me/abdalla_study2_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
8165706306:AAG-DYKXzX0Ro0Zkxbld7vTH6ryKevtQoww
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["المرحلة الأولى"],
        ["المرحلة الثانية"],
        ["المرحلة الثالثة"],
        ["المرحلة الرابعة"],
    ]

    await update.message.reply_text(
        "مرحباً بك في بوت الجامعة\nاختر المرحلة الدراسية:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"اخترت: {text}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages))

print("Bot is running...")
app.run_polling()
