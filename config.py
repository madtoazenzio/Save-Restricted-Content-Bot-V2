# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "7236453"))
API_HASH = getenv("API_HASH", "33010a70e94f80e55145980072cce969")
BOT_TOKEN = getenv("BOT_TOKEN", "7166294138:AAHM32pCpz51w0T6UOhOYmNqhXMjeDzV4Ns")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
