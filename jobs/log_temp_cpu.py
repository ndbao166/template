import os
import time
from loguru import logger


if __name__ == "__main__":
    logger.info("🚀 Starting cron job...")
    while True:
        result = os.popen("vcgencmd measure_temp").read()
        logger.info(f"🔍 CPU temperature: {result}")
        time.sleep(1)
