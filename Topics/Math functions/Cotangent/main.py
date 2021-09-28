from math import sin
from math import cos
from math import pi
HALF_THE_CIRCLE = 180
angle = float(input()) * pi / HALF_THE_CIRCLE
print(round(cos(angle) / sin(angle), 10))
