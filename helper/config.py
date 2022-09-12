from . import *

BOT_TOKEN ="5509916510:AAG2fow3mScpTf3VzMnDzAGO99nPZnYLIxw"
API_HASH ="74a2665339484da3eaaed5f4fe16da79"
APP_ID = 14560088
LOG_CHANNEL = "-1001715617029"


try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    OWNER = config("OWNER_ID", default=1322549723, cast=int)
    LOG = config("LOG_CHANNEL", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
