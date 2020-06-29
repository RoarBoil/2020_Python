# encoding: utf-8
'''
Author :    xumingjie 
Purpose:    Use generator to generate random data set.Then store the data set in MongoDB and screen it.
Created:    2020/6/27 19:59    
'''
import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")    # 连接本地数据库
mydb =myclient["xmjhomework"]   # 创建名为‘xmjhomework’的数据库
dblist = myclient.list_database_names()
if 'xmjhomework' in dblist:
    print("创建数据库成功")
mycol = mydb['mydata']  # 创建名为‘mydata’的表
mycol.drop()    # 每次跑前清空表以更新数据


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: The data type of the random value we want to get.
    :param datarange: The data range of the random value we want to get.
    :param num: The number of random values we want to get.
    :param strlen: If we want to get a random value of type string, this parameter is the length of the string.
    :return:data list
    '''
    try:
        result = list()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                # result.append(item)
                yield item
                continue
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                # result.append(item)
                yield item
                continue
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                # result.append(item)
                yield item
                continue
        else:
                pass
    except TypeError:
        print("Type Wrong!")
    except MemoryError:
        print("Memory Exception!")
    except ValueError:
        print("num Wrong!")



def dataScreening(datatype, *conditions):  # *args 可变参数，可输入n个条件
    """
    :Description: Dataset filtering.
    :param datatype:Dataset's type that need to be filtered.
    :param conditions:The conditions under which we screen
    :return:data set
    """
    result = set()
    it = iter(conditions)
    # Screening
    try:
        if datatype is int or datatype is float:
            for i in mycol.find({"data": {"$gt": next(it), "$lt": next(it)}}):
                result.add(i['data'])
        elif datatype is str:
            for tmp in conditions:
               for i in mycol.find({"data": {"$regex": tmp}}):
                        result.add(i['data'])
    except TypeError:
        print("Type Wrong!")
    except MemoryError:
        print("Memory Exception!")
    return result


def apply():
    # int
    resultint = list()
    tmpint = dataSampling(int, (1, 100), 100)
    print("\n随机生成100个在1到100之间的随机数")
    while len(resultint) < 100:
        resultint.append(next(tmpint))
    print(resultint)

    # float
    resultfloat = list()
    tmpfloat = dataSampling(float, [0.1, 99.9], 100)
    print("\n随机生成100个在0.1到99.99的随机浮点数")
    while len(resultfloat) < 100:
        resultfloat.append(next(tmpfloat))
    print(resultfloat)

    # str
    resultstr = list()
    tmpstr = dataSampling(str, string.ascii_letters + string.digits, 100, 15)
    print("\n随机生成100个长度为15的字符串")
    while len(resultstr) < 100:
        resultstr.append(next(tmpstr))
    print(resultstr)

    # 向数据库中插入数据
    for mydict_int in resultint:
        mycol.insert_one({'datatype': 'int', 'data': mydict_int})
    for mydict_float in resultfloat:
        mycol.insert_one({'datatype': 'float', 'data': mydict_float})
    for mydict_str in resultstr:
        mycol.insert_one({'datatype': 'str', 'data': mydict_str})

    # 从数据库里提取并筛选
    screenint = dataScreening(int, 25, 75)
    print("\n筛选出在25到75范围内的随机数")
    print(screenint)

    screenfloat = dataScreening(float, 33.3, 66.6)
    print("\n筛选出在33.3到66.6范围内的随机浮点数")
    print(screenfloat)

    screenstr = dataScreening(str, 'xv','py')
    print("\n筛选出含有“xv”或”py“的字符串")
    print(screenstr)

apply()
