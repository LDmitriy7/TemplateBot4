import logging

import handlers
import middlewares
import tasks
from assets import logger
from telebot import run

logging.basicConfig(level=20)

handlers.setup()
tasks.setup()
middlewares.setup()

logger.info("Starting up...")
run()
