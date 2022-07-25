# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
"""
模块功能：实现从Excel用例写入到yaml里面
"""
import os
import yaml
from common.log_handler import logger
from common.read_conf import ReadConfig
from common.read_data import ReadExcel

logger = logger


class WriteToYaml:
    def __init__(self):
        pass

    # 将excel的用例写道yaml文件中，所有的excel中的用例生成一个yaml文件.
    # 动态生成的yaml文件名和excel名一样
    @staticmethod
    def write_to_yaml():  # 传入文件名
        # 获取到测试用例数据，以及输出的yaml文件
        conf = ReadConfig()
        yaml_out_path = conf.read_info('file_path', 'yaml_path')
        cases = ReadExcel().read_excel_2()[0]
        out_yaml_file = yaml_out_path + 'test_case' + '.yml'
        try:
            with open(out_yaml_file, 'w', encoding='utf-8') as f:
                # sort_keys可以使写入数据正确排序，allow_unicode避免中文写入乱码
                yaml.dump(data=cases, stream=f, allow_unicode=True, sort_keys=False)
                logger.info('写入测试数据成功')
        except Exception as e:
            logger.info('写入测试数据失败')
            raise e
        else:
            logger.info('写入测试数据成功')

    @staticmethod
    def pos_yaml(file_list):  # 传入excel文件名的列表
        # 获取文件到测试用例数据，以及输出的yaml文件
        conf = ReadConfig()
        yaml_out_path = conf.read_info('file_path', 'yaml_path')
        for file_name in file_list:
            name = os.path.splitext(file_name)[0]
            yaml_name = str(name) + ".yml"
            out_yaml_file = yaml_out_path + yaml_name
            cases = ReadExcel().read_excel_3(file_name)
            try:
                with open(out_yaml_file, 'w', encoding='utf-8') as f:
                    # sort_keys可以使写入数据正确排序，allow_unicode避免中文写入乱码
                    yaml.dump(data=cases, stream=f, allow_unicode=True, sort_keys=False)
                    logger.info('写入测试数据成功')
            except Exception as e:
                logger.info('写入测试数据失败')
                raise e
            else:
                logger.info('写入测试数据成功')


if __name__ == '__main__':
    WriteToYaml().pos_yaml(['pitpat-1.xlsx', 'pitpat-2.xlsx'])