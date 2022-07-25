# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ
from common.log_handler import logger


logger = logger


class DealDepend(object):

    @staticmethod
    def deal_data(is_db, change_word, sql, body, case_id, depend, sr, db_init):
        # 判断depend字段是否为字典类型，不是就转成字典
        if isinstance(depend, dict):
            pass
        else:
            if depend is None:
                pass
            else:
                depend = eval(depend)

        # 判断body字段是否为字典类型，不是就转成字典
        if isinstance(body, dict):
            pass
        else:
            if body is not None:
                body = eval(body)

        # 【判断依赖类型】
        # 1 是否数据库依赖
        if is_db == 1:
            # 判断依赖字段是否为空， 说明只执行sql
            if change_word is None:
                db_init.deal_sql(sql)
                logger.info('已执行SQL：%s', sql)

            else:
                # 把excel的change_word字段分割
                update_words = change_word.split(',')
                msg = db_init.get_one(sql)
                for field in range(len(msg)):
                    if isinstance(body, dict):
                        body[update_words[field]] = msg[field]
                    else:
                        pass
                logger.info('用例%s请求值为%s：' % (case_id, body))

        # 2 是否接口依赖
        elif {} != depend:
            temp = sr.read_depend_data(depend)
            # 合并字典
            body = dict(body, **temp)
            logger.info('用例%s请求值为%s：' % (case_id, body))
            # 保存实际的请求body
            sr.save_body(case_id, body)
        else:
            # 3 没有依赖，不需要修改body
            logger.info('用例%s请求值为%s：' % (case_id, body))
        return body
