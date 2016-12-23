from pprint import pprint
def gets(l, i):
  v = int(l[6:int(l.find('g'))-1])
  #print(v)
  b = l[int(l.find('b')):]
  if b in i.keys():
    s = i.pop(b)
    print(s)
    i[b] = list([s, v]).sort()
  if b not in i.keys():
    i[b] = int(v)
  #print(inv)
  #print('linebreak')

def gives(l, i):
  bg = l[:int(l.find('g'))-1]
  bl = l[int(l.find('l'))+7:int(l.find('a'))-1]
  #print(bl)
  bh = l[int(l.find('h'))+8:]
  #print(bh)
  if bg in i.keys():
    g = i.pop(bg)     
    if type(g) == 'list':
      #if int(17) and int(61) in g: print(bg)
      #if int(17) or int(61) in g: print(bg)
      if bl in i.keys(): 
        o = i.pop(bl)
        #print(o)
        #print(list([int(l), int(g[0])]).sort())
        i[bl] = list([int(o), int(g[0])]).sort()
      else: i[bl] = list([int(g[0]), int(g[0])])
      if bh in i.keys():
        h = i.pop(bh)
        i[bh] = list([int(l), int(g[1])]).sort()
      else: i[bh] = list([g[1], g[1]])
    elif type(g) == int:
      g = int(g)
      g = list([g])*2
      if bl in i.keys(): 
        o = i.pop(bl)
        i[bl] = list([int(o), int(g[0])]).sort()
      else: i[bl] = g[0]
      if bh in i.keys():
        h = i.pop(bh)
        i[bh] = list([int(h), int(g[1])]).sort()
      else: i[bh] = g[1]
    else: 
      print(g) 
      print(type(g))
  elif bg not in i.keys():
    g = [0,0]
    if bl in i.keys(): 
        o = i.pop(bl)
        print(o)
        print(g[0])
        i[bl] = [o, g[0]].sort()
    else: i[bl] = g[0]
    if bh in i.keys():
        h = i.pop(bh)
        i[bh] = [int(h), int(g[1])].sort()
    else: i[bh] = g[1]
  else: 
    #print(bg)
    print('ERROR')  
       
         
   #else:
        
with open('..\input\input.txt') as data:
  data = data.read().splitlines()
  inv = dict() #inventories
  for line in data:
    if line.startswith('value'):
      gets(line, inv)
    if line.startswith('bot'):
      gives(line, inv)  
    #pprint(inv)
    #print(inv)
    #if [17,61] in inv.keys():
    #  print(inv)