# Programming Assignment 2: Robot and the Charger
import math
n = int(input())
move = []
originX = 0
originY = 0

for i in range(n):
  direction,step = input().split()
  if direction == 'UP':
    originY = originY + int(step)
  if direction == 'DOWN':
    originY = originY - int(step)
  if direction == 'LEFT':
    originX = originX - int(step)
  if direction == 'RIGHT':
    originX = originX + int(step)

print(round(math.sqrt(originX*originX+originY*originY)),end="")