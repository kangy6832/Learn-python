import random

a = random.randrange(1, 101)
count = 0
while True:
    b = int(input("请输入一个整数："))
    count += 1
    if b > a:
        print("太大了!")
    elif b < a:
        print("太小了!")
    else:
        print(f"恭喜你，猜对了！你总共猜了{count}次。")
        break
