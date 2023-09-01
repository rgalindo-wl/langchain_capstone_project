import logging
import os
from pathlib import Path

from dotenv import load_dotenv

### COMMON PATHS
ROOT_PATH = str(Path(__file__).parent.parent)
DATA_PATH = ROOT_PATH + "/data/"
RAW_PATH = DATA_PATH + "raw/"


load_dotenv(ROOT_PATH + "/.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""


def configure_logger(name: str) -> logging.Logger:
    """Configurates logger with a custom name

    Args:
        name (str): A name for the logger

    Returns:
        logging.Logger: A configured logger object
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
