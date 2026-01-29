import telegram
from telegram import Bot
from telegram.ext import ApplicationBuilder
import logging

logging.basicConfig(level=logging.INFO)

def test():
    print(f"Propagated Telegram Version: {telegram.__version__}")
    
    print("Testing Bot instantiation...")
    try:
        bot = Bot("123:ABC")
        print("Bot instantiated successfully.")
    except Exception as e:
        print(f"Error instantiating Bot: {e}")

    print("Testing ApplicationBuilder...")
    try:
        app = ApplicationBuilder().token("123:ABC").build()
        print("Application built successfully.")
    except Exception as e:
        print(f"Error building app: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test()
