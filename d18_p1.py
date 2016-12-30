from pprint import pprint
rows = list()
rows.append(finput)
def flooring(r):
  p = '.'+r[(len(r)-1)]+'.'
  next = list()
  for i,c in enumerate(p[1:101],start=1):
    if p[i-1] == '^' and c == '^' and p[i+1] == '.': next.append('^')
    elif p[i-1] == '.' and c == '^' and p[i+1] == '^': next.append('^')
    elif p[i-1] == '^' and c == '.' and p[i+1] == '.': next.append('^')
    elif p[i-1] == '.' and c == '.' and p[i+1] == '^': next.append('^')
    else: next.append('.')
  r.append(''.join(next))
def rowcount(r):
  return r.count('.') 

while len(rows) < 40:
  flooring(rows)

print(sum(map(rowcount, rows)))
