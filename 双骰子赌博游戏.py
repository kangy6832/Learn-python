import random
money = 1000

while money > 0:
    print(f'你现在有{money}元')
    while True:
        debt = int(input('请输入你要赌的钱数：'))
        if debt > money:
            print('你没有那么多钱，请重新输入')
            continue
        elif debt <= 0:
            print('请输入一个正数')
            continue
        else:
            break

    first_point = random.randrange(1,7) + random.randrange(1,7)
    print(f'你掷出了{first_point}点')
    if first_point in [7, 11]:
        print('你赢了！')
        money += debt
    elif first_point in [2, 3, 12]:
        print('你输了！')
        money -= debt
    else:
        print(f'继续掷骰子')
        while True:
            point = random.randrange(1,7) + random.randrange(1,7)
            print(f'你掷出了{point}点')
            if point == first_point:
                print('你赢了！')
                money += debt
                break
            elif point == 7:
                print('你输了！')
                money -= debt
                break
print('你破产了！')