##!/usr/bin/python3
"""
  Author: DY.Xu
  Purpose: Data generation and Screening
  Created: 15/6/2020
"""
import random,string

def dataSampling(datatype, datarange, num, strlen = 12):
    '''
            :Description: Generate a given condition random data set.
            :param datatype: basic data type (int  float  str)
            :param datarange: iterable data set
            :param num: number of data
            :param strlen:string length
            :return a data set
        '''
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        else:
            raise NameError
    except TypeError:
        print("Please enter the iterable data range in dataSampling")
    except NameError:
        print("Please enter the correct data type in dataSampling")
    except Exception:
        print("There are other errors in dataSampling")
def dataScreening(datatype, datarange, num, *args):
    '''
                :Description: Screen the data set
                :param data: An iterable data set
                :param args: Iterable ranges
                :return a data set
            '''
    try:
        data=dataSampling(datatype, datarange, num)
        result = []
        for n in range (num):
            item=next(data)
            for i in args:
                if type(i) is set or list or tuple:
                    try:
                        it = iter(i)
                        if item >= next(it) and item <= next(it):
                            result.append(item)
                            break
                    except StopIteration:
                        pass
                elif type(i) is str:
                    if i in item:
                        result.append(item)
                        break
                else:
                    raise NameError
    except NameError:
        print("Please enter the correct data type in dataScreening")
    except TypeError:
        print("Please enter the correct condition type in dataScreening")
    except Exception:
        print("There are other errors in dataScreening")
    else:
        return result
def Apply():
    # #a1 = dataSampling(int, (0, 100), 30)
    result1 = dataScreening(int, (0, 100), 30, (0, 60))
    # # a2 = dataSampling(float, (0, 100), 20)
    result2 = dataScreening(float, (0, 100), 20, (0, 50))
    a3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10, 6)
    result3 = dataScreening(str, string.ascii_letters + string.digits + "@#$!",20, 'at', 's', 'c')
    print("type:int range:(0, 60)\n", result1)
    print("type:float range:(0, 50)\n", result2)
    print("type:string range:'a' 'at'\n", result3)

if __name__ == '__main__':
    Apply()
