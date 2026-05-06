# 暴力解法
# for x in range(0, 21):
#     for y in range(0, 34):
#         for z in range(0, 101, 3):
#             if x + y + z == 100 and 5*x + 3*y + z//3 == 100:
#                 print(f'公鸡{x}只，母鸡{y}，小鸡{z}')


for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if 5*x + 3*y + z//3 == 100 and z%3==0:
            print(f'公鸡{x}只，母鸡{y}，小鸡{z}')