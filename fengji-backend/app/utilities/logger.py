import os
import logging
from logging import handlers
from app.config import app_config


def create_logger(log_file='fengji-backend.log'):
    pwd = os.getcwd()
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a standard formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s')

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Create a file handler
    file_handler = handlers.RotatingFileHandler(os.path.join(pwd, 'app', 'tmp', log_file),
                                                mode='a',
                                                maxBytes=app_config.LOGGING['MAX_LOG_SIZE'] * 1024,
                                                backupCount=app_config.LOGGING['BACKUP_COUNT'],
                                                encoding=None)

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Attach the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
