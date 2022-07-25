# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ


# 函数工具类模块
import base64
import hashlib
import json
import os
import time
from datetime import datetime
import yaml


# 写
def write_yaml(path, content):
    with open(path, 'w', encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)


# path 为文件路径+文件名 读取josn文件
def read(path):
    with open(path, 'r', encoding="UTF-8") as f:
        json_dict = json.load(f)
        # result = json.dumps(json_dict, indent=4)
    return json_dict


# 获取项目common路径
def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


# 获取项目pitpat路径
def get_path_dir():
    path_dir = os.path.dirname(os.path.dirname(__file__))
    return path_dir


# md5加密
def get_md5(pws=None):
    """
    主要是密码等字符串进行加密处理
    :param pws: 密码
    :return: 加密之后的结果
    """
    # 调用加密方法
    if pws is None:
        return None
    else:
        md5 = hashlib.md5(pws.encode('UTF-8'))
        return md5.hexdigest()


# 文件进行加密
def file_md5(path):
    with open(path, 'rb') as f:
        m = f.read()  # rb表示用二进制打开
        res = hashlib.md5(m).hexdigest()  # 使用二进制打开，加密时不需要用encode
    return res


# base64加密
def encode_base64(pws):
    re = base64.b64encode(pws.encode()) # 加密
    result = re.decode()  # 加密后的结果
    return result


# 解密
def decode_base64(pws):  # pws：密文
    m = base64.b64decode(pws) # 解密
    return m.encode()


# 返回公共部分headers
def common_headers():
    headers = {
            "email": 'plz123456@163.com',
            "hasAppLogin": "OKey"
        }
    return headers


# 将日期转化为时间戳
def data_transform_timestamp(time_):
    """
    将日期转化为时间戳
    :param time_:  日期 ：2020-08-20
    :return: 时间戳（日期）
    """
    time_stamp = float(time_ / 1000)
    time_array = time.localtime(time_stamp)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return other_style_time


# 将时间转化为时间戳(精确到毫秒)
def time_transform_timestamp(time_):
    """
    将日期转化为时间戳
    :param time_:  可以为时间： 2019-01-14 15:22:18.123，
    :return: 时间戳（时间）
    """
    time_obj = datetime.strptime(time_, "%Y-%m-%d %H:%M:%S.%f")
    obj_stamp = int(time.mktime(time_obj.timetuple()) * 1000.0 + time_obj.microsecond / 1000.0)
    return obj_stamp


# if __name__ == '__main__':
    # a = get_md5('plz123456')
    # print(a)
    # a = time_transform_timestamp('2022-04-21 00:00:00.000')
    # print(a)

