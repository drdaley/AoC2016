#Bathroom Security

keypad= [[1,2,3],[4,5,6],[7,8,9,]]
#start at keypad[1][1]
direction = ['U','D','L','R']
move = [(1,0),(-1,0),(0,-1),(0,1)]
code= list()

def digit():
  coordinates = [1,1]
  for i in range(len(instruction)):
    for d in range(len(coordinates)):
      coordinates[d] += move[direction.index(instruction[i])][d]
    for d in range(len(coordinates)):
      if coordinates[d] > 2 : coordinates[d] = 2
      if coordinates[d] < 0 : coordinates[d] = 0
  code.append(keypad[coordinates[0]][coordinates[1]])
  
input = open('input.txt') 
data = input.read()
instructions = data.strip('\n').split('\n')
for i in range(len(instructions)):
  instruction=instructions[i]
  digit()

print(str(code[0:]))

