# Day 7: Internet Protocol Version 7
def check(s, value):
  for c in range(len(s)-3):
    
    if s[c] != s[c+1] and s[c:c+2] == str(s[c+3]+s[c+2]): 
      value.append('T')
with open('..\input\input.txt') as data:
  linedata = data.read().splitlines()
  counter = 0
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
    invalue = list()
    for o in outside:
      check(o, outvalue)
    for i in inside:
      check(i, invalue)
    print(outside)
    print(inside)
    if 'T' in outvalue and 'T' not in invalue: 
      counter = counter + 1
print(counter)  