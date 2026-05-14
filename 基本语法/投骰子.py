import random

countes = [0] * 6
for i in range(1000000):
    face = random.randrange(1, 7)
    countes[face - 1] += 1
    
for count in countes:
    print(count)