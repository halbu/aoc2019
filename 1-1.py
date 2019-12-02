from aoctools import *
import math

data = ld("1-1")
print(sum([(math.floor(int(d) / 3) - 2) for d in data]))