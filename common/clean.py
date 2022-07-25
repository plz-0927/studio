# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
import os
import shutil
from common.log_handler import logger
"""
需求：清除原来的测试结果数据
逻辑：遍历指定目录下的文件和文件夹， 一一删除
"""


logger = logger


class ProDo:

    @staticmethod
    def remove_allure(*args):
        for ar in args:
            for f in os.listdir(ar):
                filepath = os.path.join(ar, f)
                if os.path.isfile(filepath):
                    os.remove(filepath)
                #  模板文件都是json格式的
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
            logger.info(f'{ar}目录下文件已全部清除')