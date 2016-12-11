# Squares With Three Sides

c = 0
raw = list()
intermediate = list()
triangles = list()
triangle  = list()

#get raw input
input = open('input.txt') 
data = input.read()
#strip lines, split into lines
raw = data.split()
intermediate.extend(raw[::3])
intermediate.extend(raw[1::3])
intermediate.extend(raw[2::3])
 
i=0
while (len(intermediate))/3 > len(triangles) :
  triangles.append(intermediate[3*i:3*i+3])
  i = i+1
for i in range(len(triangles)) : triangles[i] = list(map(int, triangles[i]))
for i in range(len(triangles)):
  triangles[i].sort()
  if sum(triangles[i][:2]) > triangles[i][2] :
    c = c + 1
  
print(c)
