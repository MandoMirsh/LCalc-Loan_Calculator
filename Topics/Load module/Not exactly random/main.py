# place `import` statement at top of the program
from random import seed
from random import randint

LOWER_BOUND = -100
UPPER_BOUND = 100

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
seed(n)
print(randint(LOWER_BOUND, UPPER_BOUND))
