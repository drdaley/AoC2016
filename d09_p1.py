def parse(d, x):
  b = d.find('(') # beginning
  e = int(d.find(')')) # end
  m = d.find('x'[b:e]) # middle
  l = int(d[b+1:m]) # length
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
    if parse(data,3) != '':
      decrypt[len(decrypt):] = parse(data,3)
    n= parse(data,1)
    t = str(parse(data,0)*n)
    if t != '':
      decrypt[len(decrypt):] = t
    data = parse(data,2)
    print(len(data))
  if '(' not in data and data != '':
    decrypt[len(decrypt):] = data
  print(len(''.join(decrypt)))