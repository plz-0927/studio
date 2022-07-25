# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ


import pymysql
from common.log_handler import logger


class MysqlConnect(object):
    conn = None
    logger = logger

    def __init__(self, host, username, password, db, charset='utf-8', port=3306):

        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.charset = charset
        self.port = port
        self.cur = None

    # 连接数据库
    def connect(self):

        try:
            self.conn = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db,
                                        port=3306)
            self.cur = self.conn.cursor()
        except Exception as e:
            return self.logger.info("Database {0} connection failed".format(e))

    # 关闭数据库连接
    def close_connect(self):
        self.cur.close()
        self.conn.close()

    # 查询一条记录
    def get_one(self, sql):
        try:
            self.connect()
            self.cur.execute(sql)
            result = self.cur.fetchone()
            self.close_connect()
        except Exception as e:
            return self.logger.info("查询报错:{0}".format(e))
        return result

    # 查询所有记录
    def get_all(self, sql):
        try:
            self.connect()
            self.cur.execute(sql)
            result_list = self.cur.fetchall()
            self.close_connect()
        except Exception as e:
            return self.logger.info("查询报错:{0}".format(e))
        return result_list

    # 编辑
    def _edit(self, sql):
        try:
            self.connect()
            count = self.cur.execute(sql)
            self.conn.commit()
            self.close_connect()
        except Exception as e:
            return self.logger.info("编辑报错:{0}".format(e))
        return count

    # 修改
    def update(self, sql):
        return self._edit(sql)

    # 插入
    def insert(self, sql):
        return self._edit(sql)

    # 删除
    def delete(self, sql):
        return self._edit(sql)
