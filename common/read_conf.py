# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
import yaml
from common.log_handler import logger

"""
读取配置文件类
"""


class ReadConfig:

    logger = logger

    def __init__(self):
        with open('../config/config.yml', 'r', encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def read_info(self, point, info):
        return self.data[point][info]
