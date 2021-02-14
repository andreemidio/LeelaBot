import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
DEBUG = os.getenv("DEBUG")
#BASE_API_URL = os.getenv("BASE_API_URL")