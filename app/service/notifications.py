import time
import requests
from ping3 import ping
from utils.logs.logging import logger
from infra.config import settings

# ****************************************************************
# Desc: Notify the network status to Telegram
# ****************************************************************

# --------------------- Sending Message ---------------------------
def send_telegrem_message(msg:any):
    url=f"{settings.TELEGRAM_URL}/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    # ***Query parameters for request******
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': msg
    }
    try:
        res=requests.post(url,data=payload)
        res.raise_for_status()
        if res.status_code == 200:
            # logger.info(res.json())
            logger.info("Message sent to telegram successfully.")
        else:
            logger.warn("Failed message sending!!!")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending message: {e}")
        
# ------------------------ Tracking Func --------------------------
def tracking_host()->bool:
    res_time=ping(settings.HOST, timeout=4) #Ping with a timeout of 4 seconds
    if res_time is not False:
        logger.info(f"Reply from {settings.HOST}: Normal running ... {res_time} ms")
        return True
    else:
        logger.warn(f"Reply from {settings.HOST}: Destination host unreachable.")
        return False