#import re

#criterion = re.compile((*?x*?) )
def parse(d,b,e,m,l,n,t,c,x):
  b = d.find('(') # beginning
  #print(b)
  
  #print(d.find(')'[b:]))
  e = int(d.find(')')) # end
  #print(d.find('x'[b:e]))
  
  m = d.find('x'[b:e]) # middle
  
  #print(m)
  #print(e)
  #print(d[b+1:m])
  l = int(d[b+1:m]) # length
  #print(l)
  
  n = int(d[m+1:e]) # times
  
  t = str(d[int(e+1):int(e+l+1)])
  
  c = (t, n, d[e+l+1:],d[:b]) #0 is t, 1 is n, 2 is after decompression string, 3 is before
  return c[x]



with open('..\input\input.txt') as data:
  data = str(data.read())
  b=0
  e=0
  m=0
  l=0
  n=0
  t=str()
  c = tuple()
  decrypt = list()
  while '(' in data:
    
    if parse(data,b,e,m,l,n,t,c,3) != '':
      decrypt[len(decrypt):] = parse(data,b,e,m,l,n,t,c,3)
    n= parse(data,b,e,m,l,n,t,c,1)
    #print(n)
    t = str(parse(data,b,e,m,l,n,t,c,0)*n)
    #print(len(t))
    if t != '':
      decrypt[len(decrypt):] = t
    data = parse(data,b,e,m,l,n,t,c,2)
    print(len(data))
  if '(' not in data and data != '':
    decrypt[len(decrypt):] = data
  #print(''.join(decrypt))
  print(len(''.join(decrypt)))