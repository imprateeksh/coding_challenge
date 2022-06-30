import logging
import os
import logging.handlers
from constants import app_constants as const


if not os.path.isdir(const.LOG_PATH):
    os.mkdir(const.LOG_PATH)

INFO_LOG = const.LOG_PATH + "/info.log"
ERROR_LOG = const.LOG_PATH + "/error.log"

class Logger:

    def __init__(self):
        Logger.create_logger(logger_name="info", file_name= INFO_LOG, level="info")
        Logger.create_logger(logger_name="error", file_name= ERROR_LOG, level="error")

    @staticmethod
    def create_logger(logger_name, file_name, level):
        if level == "info":
            level = logging.INFO

        if level == "error":
            level = logging.ERROR
        
        log_val = logging.getLogger(logger_name)
        formatter = logging.Formatter(const.LOG_FORMATTER)

        file_handler = logging.FileHandler(file_name, mode='a')
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        log_val.setLevel(level)

        if not log_val.hasHandlers():
            log_val.addHandler(file_handler)
            log_val.addHandler(console_handler)
        
        return log_val
    
    @staticmethod
    def info(msg):
        log = logging.getLogger("info")
        log.info(msg)
    
    @staticmethod
    def error(msg):
        log = logging.getLogger("error")
        log.info(msg)
