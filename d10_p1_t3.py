from pprint import pprint
def gets(l, i): # old function
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
  
  
def parval(l): # parses value (line) into (value, bot) 
  return (int(l[6:int(l.find('g'))-1]), l[int(l.find('b')):])
def parbotexc(l): #parses exchange (line) into (l-bot, h-bot)
  return (l[int(l.find('l'))+7:int(l.find('a'))-1],l[int(l.find('h'))+8:])

def gives(l, i): # old function
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
def frominv(b, inv): #(bot, inventories) in and returns (low, high)
  if b in inv.keys():
    if len(inv[b]) == 2:
      t = inv.pop(b)
      l = t[0]
      h = t[1]
      return (l, h)      
    elif len(inv[b]) == 1:
      t = inv.pop(b)
      l = t[0]
      h = t[0]
      return (l, h)
    else: print('frominv error')
  elif b not in inv.keys():
    return (0,0)
  else: print('frominv error')    
def intoinv(b, v, inv): #(bot, value, inventories) and puts the item into the bot's inventory
  if b in inv.keys(): 
    t = inv.pop(b)
    #print(t)
    #print(t[0])
    #print(int(t[0]))
    #print(sorted([int(t[0]), v]))
    inv[b] = sorted([int(t[0]), v])
    #print(inv[b])
  elif b not in  inv.keys():
    inv[b] = [v]
  else: print('intoinv error')
  if [17, 61] in inv.values(): print('Bot of interest: '+b)
  #pprint(inv)
  
  
with open('..\input\input.txt') as data:
  data = data.read().splitlines()
  inv = dict() #inventories
  for line in data:
    if line.startswith('value'):
      v = parval(line)
      intoinv(v[1], v[0], inv)
    elif line.startswith('bot'):
      b = parbotexc(line)
      lh= frominv(line[:int(line.find('g'))-1], inv)  
      intoinv(b[0], lh[0], inv)
      intoinv(b[1], lh[1], inv)
    #pprint(inv)
    #print(inv)
    
#pprint(inv)