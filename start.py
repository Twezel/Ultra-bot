from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

async def start(update, context):

    keyboard = [
        [InlineKeyboardButton("🔍 بحث", callback_data="search")],
        [InlineKeyboardButton("📚 متابعاتي", callback_data="mylist")],
        [InlineKeyboardButton("🔥 آخر التحديثات", callback_data="latest")]
    ]

    await update.message.reply_text(
        "أهلاً بك في بوت المانهوا 📚",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

start_handler = CommandHandler("start", start)
