# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
import json
from common.log_handler import logger
import requests

logger = logger


class HttpClient:
    """
    request主要是对requests库进行二次封装，属于框架底层代码
    """
    def __init__(self):
        self.session = requests.session()

    def send_request(self, host, path, method, body, params_type='form', **kwargs):
        # 定义参数
        url = host + path
        method = method.upper()
        params_type = params_type.upper()
        # 如果body是字符串就转换成字典
        if isinstance(body, str):
            body = json.loads(body)
        if 'GET' == method:
            response = self.session.request(method=method, url=url, data=body, timeout=3, **kwargs)
            resp = response.json()

        elif 'POST' == method:
            if 'FORM' == params_type:
                response = self.session.request(method=method, url=url, data=body, timeout=3, **kwargs)
                resp = response.json()
            else:
                response = self.session.request(method=method, url=url, json=body, timeout=3, **kwargs)
                resp = response.json()

        else:
            raise ValueError('request method "{}" error'.format(method))

        # 打印接口日志
        logger.info(f'requestUrl={url}, requestHeaders={response.headers} requestMethod={method}, params={body}, '
                    f'response={resp}')
        return resp

    def __call__(self, method, url, params_type='form', body=None, **kwargs):
        return self.send_request(method, url, params_type, body, **kwargs)

    def close_session(self):
        self.session.close()







