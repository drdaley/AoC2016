import numpy as np

#def parse(d,b,e,m,l,n,t,c,x):
#  b = d.find('(') # beginning
#  e = int(d.find(')')) # end
#  m = d.find('x'[b:e]) # middle
#  l = int(d[b+1:m]) # length
#  n = int(d[m+1:e]) # times
#  t = str(d[int(e+1):int(e+l+1)])
#  c = (t, n, d[e+l+1:],d[:b]) #0 is t, 1 is n, 2 is after decompression string, 3 is before
#  return c[x]

#def findmore()
  
def seqisolate(d): #looks to find an entire chunk where decompression flags will act on each other
  b = int(d.find('(')) # beginning
  e = int(d.find(')')) # end 
  m = int(d.find('x'[b:e])) # middle
  l = int(d[b+1:m]) # length
 #c = d.count('('[e+1:e+1+l])
  q = e+1 # moving end
  n = int(l+e+1) # moving end-of-sequence
  while '(' in d[q:n]:
    bt = int(d.find('(',q,n)) # beginning-temporary
    et = int(d.find(')',q,n)) # end-temporary
    mt = int(d.find('x',bt,et)) # middle-temporary
    lt = int(d[bt+1:mt]) #length-temporary 
    if et+lt > n : n = et+lt  # move up the end-of-sequence if necessary
    q = et+1 # move up temporary end
    print(n)
  print(d[b:n])
  return d[b:n]
    

def decompress(s):
  act = np.ones((s.count('('), 3),dtype=np.int16)
  print(act)


with open('..\input\input.txt') as data:
  sequence = str()
  data = str(data.read())
  
  while '(' in data:
    s = str()
    s = seqisolate(data) 
    decompress(s)
    
  