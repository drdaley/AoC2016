# No Time for a Taxicab
# need this to evaluate the argvalues
import sys
# coordinate system
x = 0
y = 0
# starting direction
facing = 'N'
compass = list['NESW']

for t in range(sys.argv[1:]):
  heading = list(sys.argv[t])
  if heading[0] == 'R':
    facing = compass[(compass.index(facing)+1)]
  elif heading[0] == 'L':
      facing = compass[(compass.index(facing)-1)]
  if facing == 'N': y += heading[1]
  elif facing == 'E': x += heading[1]
  elif facing == 'S': y -= heading[1]
  elif facing == 'W': x -= heading[1]

print(abs(x)+abs(y))
