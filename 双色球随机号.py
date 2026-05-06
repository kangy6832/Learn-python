# import random

# red_balls = list(range(1, 34))
# select_ball = []
# for i in range(6):
#     index = random.randrange(len(red_balls))
#     select_ball.append(red_balls.pop(index))

# select_ball.sort()
# for ball in select_ball:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=" ")
# blue_ball = (random.randrange(1, 17))
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

import random

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

select_balls = random.sample(red_balls, 6)
select_balls.sort()

for ball in select_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=" ")

blue_ball = random.choice(blue_balls)
print(f'\033[034m{blue_ball:0>2d}\033[0m')