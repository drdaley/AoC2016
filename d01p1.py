# No Time for a Taxicab
# need this to evaluate the argvalues
import sys
# coordinate system
x = 0
y = 0
# starting direction
facing = 'N'
compass = ['N','E','S','W']

for t in range(len(sys.argv[1:])):
  heading = list(sys.argv[t+1])
  distance = float((''.join(heading[1:])).strip(','))
  if heading[0] == 'R':
      facing = compass[((compass.index(facing)+5)%4)]
  elif heading[0] == 'L':
      facing = compass[((compass.index(facing)+3)%4)]
  if facing == 'N': y += distance
  elif facing == 'E': x += distance
  elif facing == 'S': y -= distance
  elif facing == 'W': x -= distance

print(abs(x)+abs(y))
