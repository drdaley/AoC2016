#Bathroom Security : part 2
keypad= [[5,z,3,z,1],
         [z,6,z,3,z],
         [A,z,7,z,4],
         [z,B,z,2,z],
         [D,z,C,z,9]]
#start at keypad[0][0]
direction = ['U','D','L','R']
move = [(-1,1),(1,-1),(-1,-1),(1,1)]
code= list()
def digit():
  coordinates = [0,0]
  for i in range(len(instruction)):
    if (for d in range(len(coordinates)): coordinates[d] += move[direction.index(instruction[i])][d] >= 0) and (for d in range(len(coordinates)): coordinates[d] += move[direction.index(instruction[i])][d] <= 0) :
      for d in range(len(coordinates)):
        coordinates[d] += move[direction.index(instruction[i])][d]
#    for d in range(len(coordinates)):
#      if coordinates[d] > 4 : coordinates[d] = 4
#      if coordinates[d] < 0 : coordinates[d] = 0
  code.append(keypad[coordinates[0]][coordinates[1]])
  
input = open('input.txt') 
data = input.read()
instructions = data.strip('\n').split('\n')
for i in range(len(instructions)):
  instruction=instructions[i]
  digit()

for i in range(len(code)) : print(str(code[i]), end='')
