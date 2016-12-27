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

def hashrep(f): #hash the imput 2016 more times, return hashed string
  #print('calling hashrep')
  #hc = 0
  e = f
  #print(e)
  for hc in range(2016):
    #print(e)
    e = hashlib.md5(e.encode(encoding="utf-8")).hexdigest()
    #print(e)
    #hc = hc+1
  return e  

salt = 'yjdafjpo'
row3hash = dict() # index, hash for hashes with 3 in a row
validhash = dict()


i = 1

while len(validhash.items()) < 64:
  f = hashlib.md5((salt+str(i)).encode(encoding="utf-8")).hexdigest()
  h = hashrep(f)
  if hashcheckone(h): 
    row3hash[i] = hashparseone(h)
  if hashchecktwo(h): 
    for (j,k) in row3hash.items():
      for c in range(len(h)-4):
        if h[c] == h[c+1] and h[c+1] == h[c+2] and h[c] == h[c+3] and h[c] == h[c+4] and h[c] == k and j >= i-999 and j != i:
          validhash[j] = hashlib.md5((salt+str(j)).encode(encoding="utf-8")).hexdigest()
          print('Found one.')

  i = i+1
pprint(sorted(validhash.items()))
print(len(validhash.items()))