# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
import os


class PRO:

    # pitpat官网
    PITPAT_URL = '********'

    # 后台登录
    BACKGRO_MANAGE_LOGIN = '*******'

    # 网关
    GATEWAY_URL = '******'


class TEST:

    # pitpat官网
    PITPAT_URL = 'https://tkjapi.ldxinyong.com/pc/index'

    # 后台登录
    BACKGRO_MANAGE_LOGIN = 'https://tkjh5.ldxinyong.com/pipat/login'

    # 网关
    # ver 1.0.0 : https://tkjapi.ldxinyong.com
    # ver 2.0.0 : https://tkjapi2.ldxinyong.com
    # GATEWAY_URL = 'http://192.168.4.160:7770'
    GATEWAY_URL = 'http://192.168.4.160:7770'


# 设置环境， 主要为了后续Jenkins集成，读取环境变量
env = os.getenv('environment', 'test')
if env == 'test':
    CONFIG = TEST
elif env == 'pro':
    CONFIG = PRO
else:
    CONFIG = TEST

