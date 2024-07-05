import time
from utils.logs.logging import logger
from infra.config import settings
from service.notifications import send_telegrem_message, tracking_host

#-------------------------- Main Func -------------------------------
def main():
    logger.info(f"Tracking Host IP: {settings.HOST}")
    while True:
        try:
            if not tracking_host():
                msg=f"Replay from {settings.HOST}: Destination host unreachable."
                send_telegrem_message(msg)
                logger.error("Host is not available")
            else:
                logger.info("Host is available")
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
        time.sleep(60) # Wait for 60 seconds before the next check

if __name__ == "__main__":
    main()