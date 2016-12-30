from pprint import pprint
finput = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
rows = list()
rows.append(finput)
total_rows = int(input('How many rows to generate? '))
def flooring(r):
  p = '.'+r[(len(r)-1)]+'.'
  next = list()
  for i,c in enumerate(p[1:101],start=1):
    if p[i-1] == '^' and c == '^' and p[i+1] == '.': next.append('^')
    elif p[i-1] == '.' and c == '^' and p[i+1] == '^': next.append('^')
    elif p[i-1] == '^' and c == '.' and p[i+1] == '.': next.append('^')
    elif p[i-1] == '.' and c == '.' and p[i+1] == '^': next.append('^')
    #if p[i-1] == '' and c == '' and p[i+1] == '':
    else: next.append('.')
  r.append(''.join(next))
def rowcount(r):
  return r.count('.') 
while len(rows) < total_rows:
  flooring(rows)
print(sum(map(rowcount, rows)))
