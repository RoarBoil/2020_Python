# -*- coding: utf-8 -*-
import random

import string
from functools import wraps


def gen_random(dtype, num, datatange=(10, 1000), str_num=8):
    """
    随机数生成
    :return:
    """

    def decorate(func):
        try:
            start, end = datatange
            if dtype is int:
                result = [random.choice(range(start, end + 1)) for _ in range(num)]

            elif dtype is float:
                result = [random.uniform(start, end + 1) for _ in range(num)]

            elif dtype is str:
                result = [''.join([random.choice(string.ascii_letters) for _ in range(str_num)]) for x in range(num)]

            else:
                result = []
                print('请参入int、float、str类型的数据')
            # print(result)
        except:
            print('传入参数错误')

        @wraps(func)
        def wrapper(dtype, datarange):
            return func(dtype, datarange, result)

        return wrapper

    return decorate


# @gen_random(int, 10)
# @gen_random(float, 10)
@gen_random(str, 10)
def random_search(dtype, datarange, result=None):
    """
    随机数搜索
    :return:
    """
    try:
        start, end = datarange
        if dtype is int:
            return [x for x in result if start <= x <= end]

        elif dtype is float:
            return [x for x in result if start <= x <= end]

        elif dtype is str:
            return [x for x in result if x.find(start) > -1 or x.find(end) > -1]

        else:
            print('请参入int、float、str类型的数据')
    except Exception as e:
        print(e)
        print('传入参数错误')


# print(random_search(int,( 20, 600)))
# print(random_search(float, (20, 600)))
print(random_search(str, ('a', 'at')))
