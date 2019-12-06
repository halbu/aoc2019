from aoctools import *

pos = [0, 0]
wiremap = {}
intersections, distances = [], []
mapping = {
  "U": [0, -1],
  "D": [0, 1],
  "L": [-1, 0],
  "R": [1, 0]
}
wires = [d.split(',') for d in ld("3-1")]

for wire in wires[0]:
  wdir, wlen = wire[0], int(wire[1:])
  for n in range(wlen):
    for x in range(2):
      pos[x] = pos[x] + mapping[wdir][x]
    if ((pos[0], pos[1]) not in wiremap):
      wiremap[(pos[0], pos[1])] = True

pos = [0, 0] # Go back to start for second wire

for wire in wires[1]:
  wdir, wlen = wire[0], int(wire[1:])
  for n in range(wlen):
    for x in range(2):
      pos[x] = pos[x] + mapping[wdir][x]
    if ((pos[0], pos[1]) in wiremap):
      intersections.append([pos[0], pos[1]])

print(min([abs(i[0]) + abs(i[1]) for i in intersections]))