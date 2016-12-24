from pprint import pprint
def copy(l,r): 
  v = l[4:l.find(' ',4)] # integer or register
  w = l[l.find(' ',4)+1:]  # register for new thing
  if v.isalpha():
#    if w in r.keys():
    del r[w]
    r[w] = r[v]
#    elif w not in r.keys():
#      r[w] = r[v]
#    else: print('copy error')
  elif v.isdigit():
    r[w] = int(v)
  else: print('copy error') 
  
def increase(l,r):
  #if 
  v = l[4:]
  w = r.pop(v) 
  r[v] = w + 1
  
def decrease(l,r):
  v = l[4:]
  w = r.pop(v) 
  r[v] = w - 1

def jumpnz(l,r,c):
  v = l[4]
  if v.isdigit():
    if v != 0:
      if l[6].isdigit():
        return c + int(l[6:]) #forward
      elif l[6] == '-':
        return c - int(l[7:]) #backwards
    else: return c + 1 
  elif v.isalpha():
    if r[v] != 0 :
      if l[6].isdigit():
        return c + int(l[6:]) #forward
      elif l[6] == '-':
        return c - int(l[7:]) #backwards
      else: print('jumpnz error')
    else: 
      return c + 1

with open('..\input\input.txt') as data:
  data = data.read().splitlines()
  cl = 0 #current line
  reg = dict()
  reg['a'] = 0
  reg['b'] = 0
  reg['c'] = 0
  reg['d'] = 0
  #print(len(data))
  while cl < len(data):
    line = data[cl]
    #print(cl)
    if line.startswith('cpy'):
      copy(line,reg)
      cl = cl + 1
    elif line.startswith('inc'):
      increase(line,reg)
      cl = cl + 1
    elif line.startswith('dec'):
      decrease(line,reg)
      cl = cl + 1
    elif line.startswith('jnz'):
      cl = jumpnz(line,reg,cl)
    else: print('mainloop error')
      
    pprint(reg)