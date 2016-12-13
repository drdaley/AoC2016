# Day 7: Internet Protocol Version 7
def abcheck(a, b, c, d, e):
  for i in a:
    for j in range(len(i)-2):
      if i[j] != i[j+1] and i[j] == i[j+2]:
        b.append('T')
        c.append(i[j:j+3])
  if 'T' in b:
    for i in d:
      for j in range(len(i)-2):
        if i[j] != i[j+1] and i[j] == i[j+2] and (str(i[j+1]+i[j]+i[j+1]) in c):
          return True
    return False
  else: return False
with open('..\input\input.txt') as data:
  counter = 0
  linedata = data.read().splitlines()
  for line in linedata:
    inside = list()
    outside = list()
    scratch = line
    while '[' in scratch:
      outside.append(scratch[0:scratch.find('[')])
      inside.append(scratch[scratch.find('[')+1:scratch.find(']')])
      scratch = scratch[(scratch.find(']')+1):]
    if scratch == '': print('Problem!')
    outside.append(scratch)
    outvalue = list()
    outid = list()
    if abcheck(outside, outvalue, outid, inside): counter = counter +1
  print(counter)  