from telegram.ext import CallbackQueryHandler

async def buttons(update, context):

    query = update.callback_query
    await query.answer()

    if query.data == "search":
        await query.message.reply_text("أرسل اسم المانهوا 🔍")

button_handler = CallbackQueryHandler(buttons)
