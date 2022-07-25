# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ

"""
封装断言的方法：

思路：
#1 遍历返回结果的每个key，
#2 根据key去预期结果找对应值
#3 比较两个结果值是否相等
"""


class AssertRe:

    @staticmethod
    def assert_job(test_result, expected):
        # 遍历返回结果的键值， 每个值进行断言
        for k, v in expected.items():
            assert v == test_result[k]
        return None


# if __name__ == '__main__':
#     AssertRe().assert_job({
#         "code": 0,
#         "data": [],
#         "msg": "成功"
#     }, {
#         "code": 1,
#         "msg": "成功"
#     })