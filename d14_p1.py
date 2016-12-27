import hashlib
from pprint import pprint
def hashcheckone(h): # is there a string of 3 in a row? T/F
  for c in range(len(h)-2):
    if h[c] == h[c+1] and h[c+1] == h[c+2]:
      #g = h[c]
      return True  
  return False    

def hashparseone(h):
  for c in range(len(h)-2):
    if h[c] == h[c+1] and h[c+1] == h[c+2]:
      return h[c]
  print('hashparse ERROR')
def hashchecktwo(h): # is there a string of 5 in a row?
  for c in range(len(h)-4):
    if h[c] == h[c+1] and h[c+1] == h[c+2] and h[c] == h[c+3] and h[c] == h[c+4]:
      #k = h[c]
      return True
  return False

  #def crossref():
  
#salt = 'abc'  
salt = 'yjdafjpo'
row3hash = dict() # index, hash for hashes with 3 in a row
#row5hash = dict() # index, hash for hashes with 5 in a row
validhash = dict()


i = 1

while len(validhash.items()) < 64:
  h = hashlib.md5((salt+str(i)).encode(encoding="utf-8")).hexdigest()
  #print(hashcheckone(h))
  #g = ''
  if hashcheckone(h): 
    row3hash[i] = hashparseone(h)
    #print(h)
    #print(row3hash.items())
    #print(str(i)+' passed hash check one.')
  if hashchecktwo(h): 
    #print(str(i)+' passed hash check two.')
    for (j,k) in row3hash.items():
      for c in range(len(h)-4):
        if h[c] == h[c+1] and h[c+1] == h[c+2] and h[c] == h[c+3] and h[c] == h[c+4] and h[c] == k and j >= i-999 and j != i:
          validhash[j] = hashlib.md5((salt+str(j)).encode(encoding="utf-8")).hexdigest()
          #print('Found one.')

  i = i+1
pprint(sorted(validhash.items()))
print(len(validhash.items()))