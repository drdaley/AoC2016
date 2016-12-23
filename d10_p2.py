from pprint import pprint
def parval(l): # parses value (line) into (value, bot) 
  return (int(l[6:int(l.find('g'))-1]), l[int(l.find('b')):])
def parbotexc(l): #parses exchange (line) into (l-bot, h-bot)
  return (l[int(l.find('l'))+7:int(l.find('a'))-1],l[int(l.find('h'))+8:])
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
def invcheck(inv, d):
  if [17,61] in inv.values():
    pprint(inv)
    print('Bot of interest found!')
    d = 'Done!'    
def stopcheck(d):
  if d == 'Done!': return True

with open('..\input\input.txt') as data:
  data = data.read().splitlines()
  inv = dict() #inventories
  for line in data: #generate a dictionary of the values that bots receive from input
    if line.startswith('value'):
      v = parval(line)
      intoinv(v[1], v[0], inv)
  while any(lineval.startswith('bot') for lineval in inv.keys()):
    for line in data: #go through data, resolve exchanges for any bot with a full inventory until the bot of interest is found
      if line.startswith('bot'):
        bg = line[:int(line.find('g'))-1] 
        if bg in inv.keys() and len(inv[bg]) == 2 :
          b = parbotexc(line)
          lh= frominv(line[:int(line.find('g'))-1], inv)  
          intoinv(b[0], lh[0], inv)
          intoinv(b[1], lh[1], inv)
    #pprint(inv)
    #print(len(inv.values()))
pprint(inv)
pprint(inv['output 0'][0]*inv['output 1'][0]*inv['output 2'][0])