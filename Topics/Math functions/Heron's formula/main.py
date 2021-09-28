# put your python code here
import math
a = int(input())
b = int(input())
c = int(input())

p = float(sum([a, b, c])) / 2
square_s = p * (p - a) * (p - b) * (p - c)
print(math.sqrt(square_s))
