# Day 13: A Maze of Twisty Little Cubicles
# How many coordinates are within 50 steps?

def pathtest(x,y,n,b,pos,f): #uses the rules from the prompt to return True for a floor and False for a wall and test whether the square is within the allowed range and test whether the path has been traveled to yet
  return (str("{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + numkey)).count('1')%2 == 0) and x >= 0 and y >= 0 and (x,y) not in b and (x,y) not in pos and (x,y) not in f
  
def genmoves(x,y): # takes x,y from adjacent and returns a list of tuples of all coordinates adjacent to c
  return [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
  
def adjacent(pos,x,y,b,f,n):
  moves = genmoves(x,y)
  for (x,y) in moves:
    if pathtest(x,y,n,b,pos,f): #pathtest each potential move
      f.append((x,y))             #if move passes, append the coordinate to forwards

numkey = 1352 
start = (1,1)
pos = [start]
backwards = [(1,1)]
steps = 0
for i in range(50):
  forwards = list()
  for (x,y) in pos:
    adjacent(pos, x,y , backwards, forwards, numkey)
  pos = forwards
  backwards.extend(pos)
print(len(backwards)) 