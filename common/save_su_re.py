# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
import jsonpath
from common.log_handler import logger


logger = logger


class SaveSuRe(object):
    def __init__(self):
        self.actual_body_1 = {}
        self.actual_body_2 = {}

    # 保存请求方法
    def save_body(self, case_id, actual_body):
        """
        保存接口请求数据：case_id和body
        :param case_id:  用例编号
        :param actual_body: 对应用例编号的请求体
        """
        # 添加一个键值对到字典
        self.actual_body_1[case_id] = actual_body

    # 保存请求返回的实际响应
    def save_response(self, case_id, actual_result):
        self.actual_body_2[case_id] = actual_result

    def read_depend_data(self, depend):
        d_k = None
        """
        :param depend:  需要依赖数据字典{"case_001":"['jsonpaht表达式1', 'jsonpaht表达式2']"}
        """
        # 定义一个函数返回的修改后的字典
        depend_dict = {}
        if depend is not None:
            if isinstance(depend, dict):
                pass
            else:
                # 转化为字典
                # 字典转为json格式的字符串
                temp = json.dumps(depend)
                # json格式字符串转为字典
                depend = json.loads(temp)

            # 判断depend字典里面是否有body字段， 有则从关联的接口取，修改body
            if 'body' in depend:
                # 对字典里面的每个键值对进行遍历
                for k, v in depend.items():
                    try:
                        # 如果键是body，就不处理
                        if k == 'body':
                            pass
                        else:
                            # 对value值进行遍历
                            for value in v:
                                logger.info('关联接口请求体的值为: %s'%self.actual_body_1)
                                # 根据value的key(case_id)去找保存请求的字典actual_body_1找到对应的值
                                actual = self.actual_body_1[k]
                                # 切片
                                d_k = value.split('.')[-1]
                                # 找到的值添加到depend_dict中
                                depend_dict[d_k] = jsonpath.jsonpath(actual, value)[0]
                    except TypeError as e:
                        logger.error(f'无法使用该表达式提取关联接口的请求数据中{d_k}值，发现异常{e}')
            else:
                for k, v in depend.items():
                    try:
                        for value in v:
                            logger.info('关联接口的响应体的值为：%s'%self.actual_body_2)
                            actual = self.actual_body_2[k]
                            # 返回依赖的接口字段key
                            d_k = value.split('.')[-1]
                            # 添加依赖到字典并返回
                            depend_dict[d_k] = jsonpath.jsonpath(actual, value)[0]
                    except TypeError as e:
                        logger.error(f'无法使用该表达式提取关联接口的响应数据中{d_k}值，发现异常{e}')
        else:
            pass
        return depend_dict
