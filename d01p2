# No Time for a Taxicab Part 2
# need this to evaluate the argvalues
import sys
# coordinate system
x = 0
y = 0
# starting direction
facing = 'N'
compass = ['N','E','S','W']
been = []
def memory(): 
  if tuple((x,y)) in been: print('x= ' + str(x) + ' y= ' + str(y) + ' distance= ' + str(int(abs(x)+abs(y))))
  else: been.append((x,y))

for t in range(len(sys.argv[1:])):
  heading = list(sys.argv[t+1])
  distance = float((''.join(heading[1:])).strip(','))
  if heading[0] == 'R':
    facing = compass[((compass.index(facing)+5)%4)]
  elif heading[0] == 'L':
    facing = compass[((compass.index(facing)+3)%4)]
  if facing == 'N':
    for z in range(int(distance)):
      y += 1
      memory()
  elif facing == 'E':
    for z in range(int(distance)):
      x += 1
      memory()
  elif facing == 'S':
    for z in range(int(distance)):
      y -= 1
      memory()
  elif facing == 'W':
    for z in range(int(distance)):
      x -= 1
      memory()
print(int(abs(x)+abs(y)))
