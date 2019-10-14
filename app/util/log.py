import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename="logs/log.txt")


def log_info(text: str):
    logging.info("Info : Time : {} Message : {}".format(get_time(), text))


def log_error(text: str):
    logging.error("Error : Time : {} Message : {}".format(get_time(), text))


def get_time():
    return datetime.now()
