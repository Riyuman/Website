from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    SESSION_STRING = getenv("SESSION_STRING")
    PORT = int(getenv("PORT", "8080"))
    BASE_URL = getenv("BASE_URL").rstrip('/')
    AUTH_CHANNEL = getenv("1968459131").split(", ")
    THEME = getenv("THEME", "flatly")
    USERNAME = getenv("USERNAME", "Suman")
    PASSWORD = getenv("PASSWORD", "Riyuman")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
