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

# Let's bruteforce this like a moron
for x in range(0, 100, 1):
  for y in range(0, 100, 1):
    new_data = data.copy()
    new_data[1] = x
    new_data[2] = y
    if (compute(new_data)[0] == 19690720):
      print("Noun: " + str(x) + ", Verb: " + str(y))
      print("Solution: " + str(100 * x + y))
