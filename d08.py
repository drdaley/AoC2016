from collections import deque
def display(s):
  for l in range(len(s)):
    print(''.join(s[l]))
def rect(h, w, s):
  for i in range(h):
    for j in range(w):
      screen[i][j] = '#'
def rrow(l, i, s):
  #temp = copy(s[l])
  #temp2 = list(map(lambda x: x = s[l][(temp.index(x)+i)%50], temp))
  #for c in s[l]:
  #  print(s[l])
  #  count = iter(range(50))
  #  temp[(next(count)+i)%50] = c
  #print(temp)
  #for c in range(len(s[l])): 
  # s[l][c] = temp[c]
  #print(s[l])
  temp = deque(s[l])
  temp.rotate(i)
  s[l] = list(temp)
  #print(s[l])
  #print(temp2)
def rcolumn(l, i, s):
  temp = list(range(6))
  for c in range(6):
    
    temp[c] = s[c][l]
  #print(temp)
  temp2 = deque(temp)
  temp2.rotate(i)
  temp = list(temp2)
  for c in range(6):
    s[c][l] = temp[c]
  #print(s[c][l])
  #temp = range(6)
  #d = iter(list(range(6)))
  #for c in range(6):
  #  temp[(next(d)+i-1)%6] = screen[c][l]
  #print(temp)
  #for c in range(6):
  #  screen[c][l] = temp[c]
    
with open('..\input\input.txt') as data:
  screen = list([['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
               ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']])
  #print(display(screen))    

  for line in data:
    if line.startswith('rect'):  
      a = line.find('x')
      
      w = int(line[a-1])
      if line[a-2].isnumeric: w = int(line[a-2:a])
      #print(w)      
      h = int(line[a+1])
      #print(h)
      rect(h,w,screen)      
    elif line.startswith('rotate row'):
      l = int(line[int(line.find('='))+1])
      if line[line.find('=')+2].isnumeric(): l = int(line[int(line.find('='))+1:int(line.find('='))+3])
      #print(l)
      i = int(line[int(line.find('b'))+3:])
      #if line[line.find('b')+4].isnumeric(): i = int(line[int(line.find('b'))+3:])
      #print(i)
      rrow(l, i, screen)
    elif line.startswith('rotate column'):
      l = int(line[int(line.find('='))+1])
      if line[line.find('=')+2].isnumeric(): l = int(line[int(line.find('='))+1:int(line.find('='))+3])
      #print(l)
      i = int(line[int(line.find('b'))+3:])
      #if line[line.find('b')+4].isnumeric(): i = int(line[int(line.find('b'))+3:])
      #print(i)
      rcolumn(l,i,screen)
  counter = 0
  for l in screen: 
     counter = counter + ''.join(l).count('#')
  print(counter)
  display(screen)    
