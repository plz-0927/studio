# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from common.os_path import OsPath


class Logger(object):

    def __init__(self, logger_name="logs"):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.backup_count = 10   # the best value of logs
        # setLevel of output
        self.console_output_level = 'WARNING'
        self.file_output_level = 'INFO'
        # setFormatter of logs
        self.log_formatter = logging.Formatter \
            ('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

    def get_logger(self):
        if not self.logger.handlers: # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.console_output_level)
            console_handler.setFormatter(self.log_formatter)
            self.logger.addHandler(console_handler)
            # 每天重新创建一个日志，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(OsPath.LOG_FILE_PATH, OsPath.LOG_FILE_NAME), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.log_formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()




