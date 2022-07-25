# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ

import pymysql
# from common.read_conf import ReadConfig


class MysqlDb:

    def __init__(self, host, port, user, passwd, db):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            passwd=passwd,
            db=db,
            autocommit=True
        )
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出cursor=pymysql.cursors.DictCursor
        self.cur = self.conn.cursor()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

# if __name__ == '__main__':
#     data_ = ReadConfig().read_ini('env.ini')
#     host_ = data_.get('mysql','HOST')
#     username_ = data_.get('mysql', 'USERNAME')
#     password_ = data_.get('mysql', 'PASSWORD')
#     db_ = data_.get('mysql', 'DB')
#     port_ = data_.get('mysql', 'PORT')
#     co = MysqlDb(host=host_, port=port_, user=username_, passwd=password_, db=db_)
#     data = co.select_db('select * from user')
#     print(data)
