"""Configuration and setup for consistent logging"""
import json
import logging

from web_app.config import DATETIME_FORMAT, config

BASIC_FORMAT = {
    "app": "new-app",
    "env": config.get_env_value("ENV"),
    "time": "%(asctime)s.%(msecs)d",
    "level": "%(levelname)s",
    "line": "%(name)s:%(funcName)s:%(lineno)d",
    "message": "%(message)s",
}


def get_logger(
    logger_name: str,
) -> logging.Logger:
    """
    Construct a basic logger.
    Args:
        logger_name:    Name of logger to instantiate
    Returns:
        Fully configured log object for JSON logging
    """
    format_dict = BASIC_FORMAT.copy()
    logger = logging.getLogger(logger_name)
    logger.setLevel(config.get_env_value("LOG_LEVEL"))
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            fmt=json.dumps(format_dict),
            datefmt=DATETIME_FORMAT,
        )
    )
    logger.addHandler(handler)
    return logger
