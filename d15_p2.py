
def lineparse(l):
  n = int(l[l.find('has')+4:l.find('p')-1])
  p = int(l[l.find('position ')+9:l.find('.')])
  return (n, p)

def dropcheck(np, t): #checks each ring if the capsule is dropped at t, returns T if all will allow the capsule passage
  pos = np.copy()
  ringcheck = list()
  for (x,(y,z)) in pos:
    if (x+z+t)%y == 0:
      ringcheck.append(True)
    else: ringcheck.append(False)
  if all(ringcheck):
    return True
  else: return False

with open('..\input\input.txt') as data:
  np = list()
  for line in data:
    np.append(lineparse(line))
  np.append((11,0))
  np = list(enumerate(np, start=1)) # gives each ring a value cooresponding to how long the capsule will take to reach it from being dropped
  t=0
  while not dropcheck(np, t):
    t=t+1
    #print('iteration')
  print(t)