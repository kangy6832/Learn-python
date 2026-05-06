num = int(input("请输入一个正整数"))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num*10 + num%10
    num //=10
    print(f'num={num}, reversed_num={reversed_num}')

print(reversed_num)