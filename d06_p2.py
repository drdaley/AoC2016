# Day 6: Signals and Noise
import collections
tabulated = list()
fcode = list()
rcode = list()
with open('input.txt') as data:
  linedata = list(map(str.rstrip, list(data.readlines())))
  for line in linedata:
    oneline = list()
    for c in line:
      oneline.append(c) 
    tabulated.append(oneline)
  tabs = list(zip(*tabulated))
  for l in tabs:
    a = collections.Counter(l)
    b = a.most_common()
    fcode.append(b[0][0])  
    rcode.append(b[len(b)-1][0])
  print(''.join(fcode))
  print(''.join(rcode))