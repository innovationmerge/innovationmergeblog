# -*- coding: utf-8 -*-
import logging
import sys
import os
from pythonjsonlogger import jsonlogger

# Custom imports

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def log_init():
    # Create Handler
    screenHandler = logging.StreamHandler(stream=sys.stdout)

    # Add a suffix which you want
    screenHandler.suffix = "%Y%m%d"

    # Create formatters and add it to handlers
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s | %(levelname)8s | %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S"
    )
    screenHandler.setFormatter(formatter)

    # Add Handler
    logger.addHandler(screenHandler)

