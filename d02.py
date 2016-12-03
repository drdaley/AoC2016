#Bathroom Security

keypad= [[1,2,3],[4,5,6],[7,8,9,]]
#start at keypad[1][1]
direction = ['U','D','L','R']
move = [(0,1),(0,-1),(-1,0),(1,0)]

def digit():
  coordinates = [1,1]
  for i in range(len(instruction)):
    for d in range[len(coordinates]:
      coordinates[d] += move[index.direction(instruction[i])][d]
    for d in range[len(coordinates]:
      if coordinates[d] > 1 : coordinates[d] = 1
      if coordinates[d] < -1 : coordinates[d] = -1
  print(keypad[coordinates[0]][coordinates[1]])
  
open('input.txt') as input: data = input.read()
instructions = data.split('n/')
  for i in range(len(instructions)):
    instructions[i]=instruction
    digit()
    

