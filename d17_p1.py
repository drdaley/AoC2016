import hashlib
#pc = input('What is the passcode? ')
pc = 'dmypynyp'
#pc = 'ihgpwlah'
c = list('UDLR') #+y,-y,-x,+x
pos = [0,0] #(x,y)
end = [3,-3]
goodpaths = list()

def findpos(path):
  pos = [0,0]
  for p in path:
    if p == 'U' : pos[1] = pos[1]+1
    elif p == 'D' : pos[1] = pos[1]-1
    elif p == 'L': pos[0] = pos[0]-1
    elif p =='R' : pos[0] = pos[0]+1
  return pos
  
def opencheck(h): #from [0:4] of the hash, returns a list, to be zipped with c, of T/F for unlocked/locked
  open = list()
  for x in h:
    if x == 'b' or x == 'c' or x == 'd' or x == 'e' or x == 'f':
      open.extend([True])
    else: open.extend([False])
  return open

def doorcheck(pos): #from pos, returns a list, to be zipped with c, of T/F if a door exists/doesn't
  doors = list()
  if pos[1] == 0: doors.extend([False,True])
  elif pos[1] == -3: doors.extend([True,False])
  elif 0 > pos[1] > -3: doors.extend([True,True])
  #print(doors)
  if pos[0] == 0: doors.extend([False,True])
  elif pos[0] == 3: doors.extend([True,False])
  elif 0 < pos[0] < 3: doors.extend([True,True])
  #print(doors)
  return doors
  
def endcheck(gp):
  for g in gp:
    if findpos(g) == [3,-3]: 
      print('The correct path is: '+g)
      return True
  return False

h = hashlib.md5((pc).encode(encoding="utf-8")).hexdigest()
open = list()
open = list(zip(c, opencheck(h[0:4]), doorcheck(pos)))
print(open)
for (d,o,t) in open:
  if all([o,t]): goodpaths.append(d)
#print(goodpaths)
s = 1 #steps    
while not endcheck(goodpaths):
  newpaths = list()
  for path in goodpaths:
    pos = findpos(path)
    #print(doorcheck(pos))
    h = str()
    h = hashlib.md5((pc+path).encode(encoding="utf-8")).hexdigest()
    open = list()
    open = list(zip(c, opencheck(h[0:4]), doorcheck(pos)))
    #print(c)
    #print(opencheck(h[0:4]))
    #print(doorcheck(pos))
    #print(open)
    for (d,o,t) in open:
      #print((d,o,t))
      #print(all([o,t]))
      if all([o,t]): 
        #print(str(path+d))
        newpaths.append(str(path+d))
  goodpaths = newpaths
  print(goodpaths)
  s = s + 1  
print(s)