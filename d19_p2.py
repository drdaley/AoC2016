import collections as co
nelves = 3014387
circle = co.deque(range(1, nelves+1))

while len(circle) > 1:
  tp = circle[0]
  lc = len(circle)
  if lc%2 == 0:
    pg = (lc/2)
    circle.rotate(int(-pg)) #brings the elf giving presents to position 0 of the deque
    circle.popleft() #removes the elf with zero presents from the deque
    circle.rotate(int(pg)) #returns the elf whose turn it is to position 0 in the deque
  elif lc%2 != 0:
    pg = ((lc/2)+0.5) #how far is present giver from the elf whose turn it is
    circle.rotate(int(-pg)) #brings the elf giving presents to position 0 of the deque
    circle.popleft() #removes the elf with zero presents from the deque
    circle.rotate(int(pg)) #returns the elf whose turn it is to position 0 in the deque
  
  circle.rotate(-1) #moves ot the next elf in turn order; should not change the outcome when the game is over
  #print(lc) #debug
print(circle[0])
