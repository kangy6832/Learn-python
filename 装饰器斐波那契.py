from functools import lru_cache
import time

# @lru_cache()
# def feib (n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# for i in range(50):
#     print(feib(i))

def record_time(func):
    def wrapp(*args, **kwargs):
        start = time.time()
        result = func()




@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))