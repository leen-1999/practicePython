

import sys
import random
from random import randint

# 01
print(f"Random Number Between 10 And 50 => {randint(10,50)}")
while True:
    r = randint(2, 10)
    if r % 2 == 0:
        print(f"Random Even Number Between 2 And 10 => {r}")
        break
while True:
    r = randint(1, 9)
    if r % 2 != 0:
        print(f"Random Odd Number Between 1 And 9 => {r}")
        break
print(dir(random))

print("#" * 30)

# 02

# 03


# 04
