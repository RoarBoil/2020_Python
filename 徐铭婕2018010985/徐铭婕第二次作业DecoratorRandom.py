# encoding: utf-8
'''
Author :    xumingjie 
Purpose:    Use decorator to generate random data set.
Created:    2020/6/20 10:25
'''

 
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num,*conditions, strlen=8):
        '''
        :Description: Generate a given condition random data set.
        :param datatype: The data type of the random value we want to get.
        :param datarange: The data range of the random value we want to get.
        :param num: The number of random values we want to get.
        :param conditions: Filter the required condition.
        :param strlen: If we want to get a random value of type string, this parameter is the length of the string.
        :return:data list
        '''
        try:
            result = list()
            if datatype is int:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.append(item)
            elif datatype is float:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.append(item)
            elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.append(item)
            else:
                    pass
        except TypeError:
            print("Type Wrong!")
        except MemoryError:
            print("Memory Exception!")
        except ValueError:
            print("num Wrong!")
        return func(result, *conditions)
    return wrapper

@dataSampling
def dataScreening(data, *conditions):  # *args 可变参数，可输入n个条件
    """
    :Description: Dataset filtering.
    :param data:Datasets that need to be filtered.
    :param conditions:The conditions under which we screen
    :return:data set
    """
    result = set()
    # Screening
    try:
        for i in data:
            if type(i) is int or type(i) is float:
                it = iter(conditions)
                if next(it) <= i <= next(it):
                    result.add(i)
            elif type(i) is str:
                for tmp in conditions:
                    if tmp in i:
                        result.add(i)
    except TypeError:
        print("Type Wrong!")
    except MemoryError:
        print("Memory Exception!")
    return result

def apply():
    # int
    print("随机生成20个在1到100之间的随机数，并筛选出在25到75范围内的随机数")
    screenint = dataScreening(int, [1, 100], 20, 25, 75)
    print(screenint)

    #float
    print("\n随机生成20个在0.1到99.99的随机浮点数，并筛选出在33.3到66.6范围内的随机浮点数")
    screenfloat = dataScreening(float, [0.1, 99.99], 20, 33.3, 66.6)
    print(screenfloat)

    #str
    print("\n随机生成20个长度为默认长度的字符串,并筛选出含有“xv”或”py“的字符串")
    screenstr = dataScreening(str, string.ascii_letters+string.digits, 20, 'xv', 'py')
    print(screenstr)

apply()
