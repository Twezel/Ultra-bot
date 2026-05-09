from telegram.ext import Application
from handlers.start import start_handler
from handlers.buttons import button_handler
from handlers.messages import message_handler
from scheduler import start_scheduler
from config import BOT_TOKEN

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(start_handler)
    app.add_handler(button_handler)
    app.add_handler(message_handler)

    start_scheduler(app)

    print("Professional Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
