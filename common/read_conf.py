# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
from configparser import ConfigParser

import yaml

"""
读取配置文件类
"""


class ReadConfig:
    def __init__(self):
        self.path_dir = '../config/'

    def read_config(self, config_filename):
        with open(self.path_dir + config_filename, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def read_ini(self, ini_filename):
        data = ConfigParser()
        data.read(self.path_dir + ini_filename)
        return data

