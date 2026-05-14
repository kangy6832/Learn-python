from functools import lru_cache

class InputError(ValueError):
    # 自定义异常类型
    pass

@lru_cache()
def fac(num):
    if num < 0:
        raise InputError("只能计算非负整数的阶乘")
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

Flag = True
while Flag:
    num = int(input('n = '))
    try:
        print(f'{num}！= {fac(num)}')
        flag = False
    except InputError as err:
        print(err)