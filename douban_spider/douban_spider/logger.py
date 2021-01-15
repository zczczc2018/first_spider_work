import sys
import logging
from time import strftime
from config import DEFAULT_LOG_FMT, DEFUALT_LOG_DATEFMT,LOG_OUT_PATH


class Logger(object):
    def __init__(self, log_type):
        self._logger = logging.getLogger()
        self.DEFAULT_LOG_FILENAME = '{0}{1}{2}.log'.format(LOG_OUT_PATH, strftime("%Y-%m-%d"), log_type)
        self.formatter = logging.Formatter(fmt=DEFUALT_LOG_DATEFMT, datefmt=DEFUALT_LOG_DATEFMT)
        self._logger.addHandler(self._get_file_handler(self.DEFAULT_LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(logging.INFO)

    def _get_file_handler(self, filename):
        filehandler = logging.FileHandler(filename, encoding='utf8')
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger