from aoctools import *

possibilities = []

for x in range(357253, 892942 + 1, 1):
  # It is a six-digit number. <- self-evidently always true
  # The value is within the range given in your puzzle input. <- self-evidently always true

  # Two adjacent digits are the same
  adjacent_similarity = False
  numstr = str(x)
  for c in range(0, 5):
    if (numstr[c] == numstr[c+1]):
      adjacent_similarity = True
    
  # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
  digits_increase = True
  for c in range(0, 5):
    if (int(numstr[c]) > int(numstr[c+1])):
      digits_increase = False

  if (adjacent_similarity and digits_increase):
    possibilities.append(x)

print(len(possibilities))