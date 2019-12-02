from aoctools import *

data = ld("2-1")
data = [int(d) for d in data[0].split(',')]

def compute(arr):
  for i in range(0, len(arr), 4):
    if (arr[i] == 99):
      return arr

    num1 = arr[arr[i+1]]
    num2 = arr[arr[i+2]]

    if (arr[i] == 1):
      arr[arr[i+3]] = num1 + num2
    elif (arr[i] == 2):
      arr[arr[i+3]] = num1 * num2

  return arr

# Restore the corrupted gravity assist program
data[1] = 12
data[2] = 2

# Get int at position 0 after execution of Intcode
print(compute(data)[0])