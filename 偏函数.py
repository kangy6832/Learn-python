import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

add = lambda x, y : x + y
add5 = functools.partial(add, 5)

print(add(5, 3))
print(add5(3))