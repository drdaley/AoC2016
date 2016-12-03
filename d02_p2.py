#Bathroom Security : part 2
#define strings
z='z'
A='A'
B='B'
C='C'
D='D'
#define keypad
keypad= [[5,z,2,z,1],
         [z,6,z,3,z],
         [A,z,7,z,4],
         [z,B,z,8,z],
         [D,z,C,z,9]]
#start at keypad[0][0]
direction = ['U','D','L','R']
move = [(-1,1),(1,-1),(-1,-1),(1,1)]
code= list()
nextmove = [0,0]
coordinates = [0,0]
def digit():
  for i in range(len(instruction)):
    for k in range(len(coordinates)): 
      nextmove[k] = (coordinates[k] + move[direction.index(instruction[i])][k])
    if all(j <= 4 for j in nextmove) and all(j >= 0 for j in nextmove):   
      for d in range(len(coordinates)):
          coordinates[d] += move[direction.index(instruction[i])][d]
  code.append(keypad[coordinates[0]][coordinates[1]])
  
input = open('input.txt') 
data = input.read()
instructions = data.strip('\n').split('\n')
for i in range(len(instructions)):
  instruction=instructions[i]
  digit()

for i in range(len(code)) : print(str(code[i]), end='')
