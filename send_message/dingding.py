# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
# 获取jenkins构建信息和本次报告地址
import base64
import hashlib
import hmac
import os
import time
import urllib.parse
import jenkins
import json
import requests


# jenkins登陆地址http://localhost:8081/jenkins/job/
jenkins_url = "http://192.168.4.50:8899/job/"
# 获取jenkins对象  username='admin', password='admin123456'
server = jenkins.Jenkins(jenkins_url, username='lzadmin', password='1q2w#E$R')
# job 名称
job_name = 'pitpat-auto'  # Jenkins运行任务名称
# job的url地址
job_url = jenkins_url + job_name
print(job_url)
# 获取最后一次构建
job_last_build_url = server.get_info(job_name)['lastBuild']['url']
print(job_last_build_url)
# allure报告地址
report_url = job_last_build_url + 'allure'  # 'allure'为我的Jenkins全局工具配置中allure别名
print(report_url)
'''
钉钉推送方法：
读取report文件中"prometheusData.txt"，循环遍历获取需要的值。
使用钉钉机器人的接口，拼接后推送text
'''


def ding_talk_send():
    d = {}
    path = os.path.abspath(os.path.dirname((__file__)))
    # 打开prometheusData 获取需要发送的信息
    f = open(path + r"/report_allure/export/prometheusData.txt", 'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    # print('运行总数:{}'.format(retries_run))
    status_passed = d.get('launch_status_passed')  # 通过数量
    # print('通过数量：{}'.format(status_passed))
    status_failed = d.get('launch_status_failed')  # 不通过数量
    # print('不通过数量：{}'.format(status_failed))
    status_broken = d.get('launch_status_broken')  # broken数量

    #  钉钉推送（测试）
    # https://oapi.dingtalk.com/robot/send?access_token=276223bcb01e6f52f5ec6f161309510ecc84efa42d51a249624345585abb5778
    # 八楼技术群
    # https://oapi.dingtalk.com/robot/send?access_token=129a082d31e53dbacf02e3bded168f419903bd5c964c92ea151acdbe1a964a4d
    # 加签
    secret1 = "SEC2a173a10b00a5cdb7c2e196127dc10db42f2ddaeaf712f4a3e60217d47373a4d"  # 八楼技术群
    # secret2 = "SEC241586137427ce7c630ee8214455c885d24fb4918d9c442578d544c3f95b55e1"  # 自动化测试群
    # access_token
    key1 = "129a082d31e53dbacf02e3bded168f419903bd5c964c92ea151acdbe1a964a4d"  # 八楼技术群
    # key2 = "276223bcb01e6f52f5ec6f161309510ecc84efa42d51a249624345585abb5778"  # 自动化测试群

    timestamp = str(round(time.time() * 1000))
    secret_enc = secret1.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret1)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote(base64.b64encode(hmac_code))
    url = f"https://oapi.dingtalk.com/robot/send?access_token={key1}&timestamp={timestamp}&sign={sign}"  # webhook
    con = {
        "msgtype": "text",
        "text": {
            "content": "pitpat-auto项目api接口自动化测试完成。"
            "\n测试概述"
            "\n运行总数：" + retries_run +
            "\n通过数量：" + status_passed +
            "\n失败数量：" + status_failed +
            "\n阻塞数量：" + status_broken +
            "\n构建地址：" + job_url +
            "\n报告地址：" + report_url
            },
        "isAtAll": True
        }
    headers = {"Content-Type": "application/json"}
    message = requests.post(url, json.dumps(con), headers=headers).json()
    return message


if __name__ == '__main__':
    ding_talk_send()
