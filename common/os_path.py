# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ

import time
from common.tools import get_path_dir


class OsPath:
    __t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()).split("-")
    __t2 = __t[2].split(" ")
    __s = f"{__t[0]}年{__t[1]}月{__t2[0]}日{__t2[1]}时{__t[3]}分{__t[4]}秒"
    __log_name = f"{__t[0]}年{__t[1]}月{__t2[0]}日"

    # 测试数据文件路径
    PROJECT_PATH = get_path_dir()

    # 日志文件名info.log
    LOG_FILE_NAME = f'{__log_name}info.log'
    # 日志路径 path = r'/Users/testfile/Desktop/auto/auto-api/log'
    LOG_FILE_PATH = f'{PROJECT_PATH}/log'
