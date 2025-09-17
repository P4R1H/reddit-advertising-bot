import logging
from logging.handlers import RotatingFileHandler
import os
import asyncio

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("async_logger")
logger.setLevel(logging.DEBUG)

file_handler = RotatingFileHandler("logs/app.log", maxBytes=5*1024*1024, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s:> %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)

async def log_info(msg):
    await asyncio.to_thread(logger.info, msg)

async def log_warning(msg):
    await asyncio.to_thread(logger.warning, msg)

async def log_error(msg):
    await asyncio.to_thread(logger.error, msg)

async def log_debug(msg):
    await asyncio.to_thread(logger.debug, msg)
