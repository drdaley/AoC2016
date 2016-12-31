import collections as co
nelves = 3014387
circle = co.deque(range(1, nelves+1))
while len(circle) > 1:
  tp = circle[0]
  
  if len(circle)%2 == 0:
    circle.rotate(int(-(len(circle)/2))) #brings the elf giving presents to position 0 of the deque
    circle.popleft() #removes the elf with zero presents from the deque
    circle.rotate(-(circle.index(tp))) #returns the elf whose turn it is to position 0 in the deque
  elif len(circle)%2 != 0:
    circle.rotate(int(-((len(circle)/2)+0.5))) #brings the elf giving presents to position 0 of the deque
    circle.popleft() #removes the elf with zero presents from the deque
    circle.rotate(-(circle.index(tp))) #returns the elf whose turn it is to position 0 in the deque
  
  circle.rotate(-1) #moves ot the next elf in turn order; should not change the outcome when the game is over
  #print(len(circle)) #debug
print(circle[0])
