# Security Through Obscurity

import re
#get raw input
input = open('input.txt') 
data = input.read()
#strip lines, split into lines
raw = data.splitlines()

values= list()
# need data in three parts [a-z], then the [0-9], then the letters in the '[]'
regex = re.compile('(\D+)([0-9]+)(\[\D+\])')

  #for each entry
for i in range(len(raw)):
  check = ['','','','']
  rs = regex.search(raw[i])
  a = (rs.group(1)).replace('-','') #makes string of the leading alphas
  #print(a)
  n = int(rs.group(2)) # makes an integer from the numbers
  #print(n)
  c = (rs.group(3)).replace('[','').replace(']','')  #sets checksum as vaiable
  #print(c)
    #for each value in the entry
  for j in range(len(c)-1):
    condition1 = len(re.findall(c[j], a)) > len(re.findall(c[j+1], a)) #number of occurances is greater
    condition2 = (len(re.findall(c[j], a)) == len(re.findall(c[j+1], a)) and str(c[j]) < str(c[j+1])) #number of occurances is the same and alphanumeric order is greater
    condition3 = len(re.findall(c[j], a)) > 0 and len(re.findall(c[j+1], a)) > 0 # makes sure checksum number (and +1) occurs in the string
    check[j] = ((condition1 or condition2) and condition3 )
    #print(re.findall(c[j], a))
  #print(check)
  #print(all(check))
  if all(check):
    values.append(n)
    

#print(values)
print(sum(values))
 
  
