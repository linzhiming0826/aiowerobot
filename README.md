### 一个简单的异步公众号框架

## 介绍

代码fork自[WeRoBot](https://github.com/offu/WeRoBot)，修改成基于sanic的异步框架

## 文档

[点我](https://aiowerobot.readthedocs.io/)

## Installation
```linux
pip install aiowerobot
```

## Simple uses
```python
from aiowerobot import AioWeRoBot

robot = AioWeRoBot(app_id='', app_secret='', token='')


@robot.handler
async def hello(message):
    return 'Hello World!'


config = {'host': '0.0.0.0', 'port': 8099}
robot.run(**config)
```