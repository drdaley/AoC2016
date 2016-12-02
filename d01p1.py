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
  if heading[0] == 'R':
      facing = compass[((compass.index(facing)+4)%3)]
  elif heading[0] == 'L':
      facing = compass[((compass.index(facing)-2)%3)]
  if facing == 'N': y += float(''.join(heading[1:]))
  elif facing == 'E': x += float(''.join(heading[1:]))
  elif facing == 'S': y -= float(''.join(heading[1:]))
  elif facing == 'W': x -= float(''.join(heading[1:]))

print(abs(x)+abs(y))
