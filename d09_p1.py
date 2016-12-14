import re

#criterion = re.compile((*?x*?) )

with open('..\input\input.txt') as data:
  data = str(data.read())
  print(data)
  while '(' in data:
    l = int(data[int(data.find('('))+1:int(data.find('x'))]) 
    t = int(data[int(data.find('x'))+1:int(data.find(')'))])
    print(l)
    print(t)
  #else