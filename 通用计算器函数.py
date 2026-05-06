def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

result = calc(0, lambda x, y : x + y, 1, 2, 3, a=4, b=5)
print(result)