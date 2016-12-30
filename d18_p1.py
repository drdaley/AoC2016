from pprint import pprint
finput = '.^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....'
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
    #if p[i-1] == '' and c == '' and p[i+1] == '':
    else: next.append('.')
  #print(len(next))
  r.append(''.join(next))
  #print(len(r))
  #previous[:0] = '.'
  #previous.extend('.')
  #print(previous)
  #print(len(previous))

while len(rows) < 40:
  flooring(rows)

#print(sum(for r in rows: r.count('.')))
def rowcount(r):
  return r.count('.')
#print(rows.count('.'))
#print(sum(lambda x: row[x].count('.')))
#pprint(rows)
print(sum(map(len, rows)))
print(sum(map(rowcount, rows)))
