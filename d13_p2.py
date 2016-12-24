# Day 13: A Maze of Twisty Little Cubicles
# How many coordinates visited in 50 steps?

def pathtest(x,y,n): #uses the rules from the prompt to return True for a floor and False for a wall
  return (str("{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + numkey)).count('1')%2 == 0)
def adjacent(pos,c,b,f,n):
  #print(c[0])
  if pathtest(c[0]+1,c[1],n) and c[0]+1 >= 0 and c[1] >= 0 and (c[0]+1,c[1]) not in b and (c[0]+1,c[1]) not in pos and (c[0]+1,c[1]) not in f:
    f.append((c[0]+1,c[1]))
  if pathtest(c[0]-1,c[1],n)  and  c[0]-1 >= 0 and c[1] >= 0 and (c[0]-1,c[1]) not in b and (c[0]-1,c[1]) not in pos and (c[0]-1,c[1]) not in f:
    f.append((c[0]-1,c[1]))
  if pathtest(c[0],c[1]+1,n)  and c[0] >= 0 and c[1]+1 >= 0 and (c[0],c[1]+1) not in b and (c[0],c[1]+1) not in pos and (c[0],c[1]+1) not in f:
    f.append((c[0],c[1]+1))
  if pathtest(c[0],c[1]-1,n)  and c[0] >= 0 and c[1]-1 >= 0 and (c[0],c[1]-1) not in b and (c[0],c[1]-1) not in pos and (c[0],c[1]-1) not in f:
    f.append((c[0],c[1]-1))
numkey = 1352 
start = (1,1)
pos = [start]
backwards = list()
steps = 0
for i in range(50):
  forwards = list()
  for c in pos:
    adjacent(pos, c, backwards, forwards, numkey)
  backwards.extend(pos)
  pos = forwards
print(backwards)
print(len(backwards)) 