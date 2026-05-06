x = int(input("请输入一个整数："))
y = int(input("请输入另一个整数："))
for i in range(x, 0, -1):
    if x%i == 0 and y%i == 0:
        print(f"{x}和{y}的最大公约数是{i}")
        break