from telegram.ext import MessageHandler, filters

async def messages(update, context):

    text = update.message.text

    await update.message.reply_text(
        f"🔍 نتيجة البحث: {text}"
    )

message_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    messages
)
