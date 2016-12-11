# Day 5: How About a Nice Game of Chess?

import hashlib
import re
r = re.compile('00000')
s = re.compile('[0-7]')
i = 0
c = 0
code = dict()
while list(map(int, code.keys())) != list(range(8)):
  h = hashlib.md5(('reyedfim'+str(i)).encode(encoding="utf-8")).hexdigest()
  i += 1
  if r.match(h) and s.match(h[5]):
    c += 1
    print(h)
    code.setdefault(int(h[5]),h[6]) 
    #print(code.items())
    print(list(map(int, code.keys())))
    #print(list(range(8)))
print(''.join(code.values()))