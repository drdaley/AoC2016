def gets(l, i):
  v = l[:int(l.find('g'))-1]
  b = l[int(l.find('b')):]
  if b in i:
    s = str(i.pop(b))
    i[b] = list([str(s), str(v)])
  if b not in i:
    i[b] = str(v)
  print(inv)

with open('..\input\input.txt') as data:
  data = data.read().splitlines()
  inv = dict() #inventories
  for line in data:
    if line.startswith('value'):
      gets(line, inv)
    #if line.startswith('bot'):
      