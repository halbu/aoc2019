from aoctools import *
import math

data = ld("1-1")

def fuel_needed(mass):
  return (math.floor(mass / 3) - 2)

def get_total_fuel(mass):
  total = 0
  fuel = fuel_needed(mass)
  while(fuel > 0):
    total = total + fuel
    fuel = fuel_needed(fuel)
  return total
  
print(sum([get_total_fuel(int(d)) for d in data]))