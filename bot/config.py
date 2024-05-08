from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("25898132"))
    API_HASH = getenv("490259e3399eb541c98cf204ddf92d75")
    BOT_TOKEN = getenv("6944321971:AAGrk5upAwXsGfMpnKaMTsv1dRVDtz4H7xI")
    SESSION_STRING = getenv("BQGLLJQALmWOSqr8ZAtaQJjlphCa6MyVEUojdUgH46_ILAMcvOO8X8jn9A5tC8TqEhRUiBBlnusKoJBlrQBm_06S0tSBWVZvd1hABZ2zNm_rCBLzSsE1BWc9N7qSUSVErYmEbB_wxkSTJ8hMnUncKbr4B3C4SK6wLckRy0_xk7bBGg6wh83kc_orOO5j7ZeRFYaXXdUEvf9Isj8hoxOEmey8CVbZUf3pZXU0YyaBybXdHBh6hDlODlJBa8z-fogX19iuVUPeXfoeDyOwzMQDcTOw-okgEhp2ikSg_rvi1KQTAhQeAA_6juwo1tv80WJyXF-DmtBfszC0daTyhODN7cCzf5LA2QAAAAE9lkijAA")
    PORT = int(getenv("PORT", "8080"))
    BASE_URL = getenv("Bhttps://suman-parvej-0f7c442b0998.herokuapp.com/").rstrip('/')
    AUTH_CHANNEL = getenv("-1001968459131").split(", ")
    THEME = getenv("THEME", "flatly")
    USERNAME = getenv("USERNAME", "Suman")
    PASSWORD = getenv("PASSWORD", "Riyuman")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
