# _*_ coding:utf-8 _*_
# !/usr/bin/python3.7
# @Email:plz0927@163.com
# @Author: Russ


from jsonschema import validators


class JsonCheck:
    def __init__(self, json_schema, json_data):
        va = validators.Draft4Validator(json_schema)
        va.validate(json_data)


if __name__ == '__main__':
    data = {
        "message": "操作成功",
        "responseCode": "0",
        "hasError": False,
        "data": {
            "id": 100123456
        }
    }
    schema = {
        "$schema": "http://json-schema.org/schema#",
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "responseCode": {
                "type": "string"
            },
            "hasError": {
                "type": "boolean"
            },
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    }
                },
                "required": ["id"]
            }
        },
        "required": ["data", "hasError", "message", "responseCode"]
    }
    a = JsonCheck(json_schema=schema, json_data=data)
    print(a)

