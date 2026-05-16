import logging
import sys
from logging import StreamHandler, FileHandler



def set_logger(name:str='task_tracker') ->logging.Logger:
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    console_handler=StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    file_handler=FileHandler("app.log")
    file_handler.setLevel(logging.INFO)

    formatter=logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger