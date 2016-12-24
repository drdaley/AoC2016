# Day 13: A Maze of Twisty Little Cubicles
# how much of the maze will I need to make to reach 31, 39

def pathtest(x,y,n): #uses the rules from the prompt to return True for a floor and False for a wall
  return (str("{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + numkey)).count('1')%2 == 0)
def adjacent(c, b, f,n):
  #print(c[0])
  if pathtest(c[0]+1,c[1],n) and c[0]+1 >= 0 and c[1] >= 0 and (c[0]+1,c[1]) not in b:
    f.append((c[0]+1,c[1]))
  if pathtest(c[0]-1,c[1],n)  and  c[0]-1 >= 0 and c[1] >= 0 and (c[0]-1,c[1]) not in b:
    f.append((c[0]-1,c[1]))
  if pathtest(c[0],c[1]+1,n)  and c[0] >= 0 and c[1]+1 >= 0 and (c[0],c[1]+1) not in b:
    f.append((c[0],c[1]+1))
  if pathtest(c[0],c[1]-1,n)  and c[0] >= 0 and c[1]-1 >= 0 and (c[0],c[1]-1) not in b:
    f.append((c[0],c[1]-1))
#"What is the mazemaker's favorite number?"
numkey = 1352 
start = (1,1)
#Where are you going?
target = (31,39) 
#minlen = target[0]- start[0] + target[1] - start[1] # the minimum distanceit will be necessary to travel if the path is a straight line
#bin = "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + numkey)
#str(bin).count('1')%2 == 0 
pos = [start]
backwards = list()
steps = 0
while target not in pos: # need to exhaust all potential paths, then step forward
  forwards = list()
  for c in pos:
    #print(c)
    #print(c[0])
    adjacent(c, backwards, forwards, numkey)
  backwards = pos
  pos = forwards
  steps = steps + 1
print(steps) 