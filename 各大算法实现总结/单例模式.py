import threading

import time


# class Singleton:
#     # _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(5)
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             # with Singleton._instance_lock:
#             Singleton._instance = object.__new__(cls)
#         return Singleton._instance

class Singleton(object):

    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

def task(arg):
    obj = Singleton()
    print(obj,str(arg))

for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()

c1 = Singleton()
c2 = Singleton()
c3 = Singleton()
c4 = Singleton()
print(id(c1),id(c2),id(c3),id(c4))


# encoding:utf-8
__author__ = 'Fioman'
__time__ = '2019/3/6 10:22'


def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
        print('这是A的类的初始化方法')


a1 = A(2)
a2 = A(3)
print(id(a1), id(a2))