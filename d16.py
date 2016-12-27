#import hashlib

def lencheck(a, hdlen): # returns false until a meets the length requirments
  if len(a) < hdlen:
    return False
  else: return True

def elongate(a): # elongates a based on given rules
  b = a[::-1]
  b = b.replace('0', 'z')
  b = b.replace('1','0')
  b = b.replace('z','1')
  #print(a+'0'+b)
  return a+'0'+b
  
def csgen(a): # takes a string and returns a string checksum based on the given rules
  ap = list(zip(a[0::2],a[1::2]))
  cs= list()
  for (x,y) in ap:
    if x == y:
      cs.append('1')
    elif x != y:
      cs.append('0')
  #print(cs)
  #print(''.join(cs))
  return ''.join(cs)
  
def cscheck(cs): # returns false unless len(cs) is odd
  if len(cs)%2 != 0: return True
  elif len(cs)%2 == 0: return False
  else: print('cscheck error')
#testinput = '10000'
input = '10111100110001111'
#testhdlen = 20
hdlen = 35651584
a = input
while not lencheck(a, hdlen):
  a = elongate(a)
a = a[:hdlen]

cs = csgen(a)
while not cscheck(cs):
  cs = csgen(cs)
print(cs)