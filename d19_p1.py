import collections as co
nelves = 3014387

circle = co.deque(range(1, nelves+1))
#print(len(circle))

while len(circle) > 1:
    circle.rotate(-1)
    circle.popleft()

print('Elf '+str(circle.popleft())+' is the winner!')

