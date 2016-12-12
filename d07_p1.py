# Day 7: Internet Protocol Version 7
def check(s, value):
  for c in range(len(s)-3):
    
    if s[c] != s[c+1] and s[c:c+2] == str(s[c+3]+s[c+2]): 
      #print(s[c:c+4])
      value.append('T')
  
with open('input.txt') as data:
  linedata = data.read().splitlines()
  counter = 0
  for line in linedata:
    inside = list()
    outside = list()
    scratch = line
    while '[' in scratch:
      print(scratch[0:scratch.find('[')])
      outside.append(scratch[0:scratch.find('[')])
      print(scratch[scratch.find('[')+1:scratch.find(']')])
      inside.append(scratch[scratch.find('[')+1:scratch.find(']')])
      scratch = scratch.lstrip(scratch[0:scratch.find(']')+1])
    print(scratch)
    if len(scratch) > 0 : outside.append(scratch)
    outvalue = list()
    invalue = list()
    #for s in outside:
    check(''.join(outside), outvalue)
    #for s in inside:
    check(''.join(inside), invalue)
    print(line)
    if 'T' in outvalue and 'T' not in invalue: 
      
      counter = counter + 1
  print(counter)  