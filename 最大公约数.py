x = int(input("请输入一个整数："))
y = int(input("请输入另一个整数："))

while x%y != 0:
    x, y = y, x%y

print(f"最大公约数是{y}")

