for i in range(100, 1000):
    low = i%10
    mid = i//10%10
    hei = i//100
    if i==low**3 + mid**3 + hei**3:
        print(i)