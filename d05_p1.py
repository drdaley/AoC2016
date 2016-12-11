# Day 5: How About a Nice Game of Chess?

import hashlib
import re
r = re.compile('00000')
i = 0
c = 0
code = list()
while c < 8:
  h = hashlib.md5(('reyedfim'+str(i)).encode(encoding="utf-8")).hexdigest()
  #print(('reyedfim'+str(i)).encode(encoding="utf-8"))
  #print(h)
  i += 1
  if r.match(h):
    c += 1
    print(h)
    code.append(h[5]) 
#print(code)
print(''.join(code))
