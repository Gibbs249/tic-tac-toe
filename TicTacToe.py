# Tic-Tac-Toe game by Andrew Gibbons
# This is a solo project I have created to show some of what I can do with Python.
# If you would like to play the game it offers a mode to play vs my algorithm
# as well as a mode to play vs a person next to you!

#imports
import random

# Game intro
print('Welcome to Tic-Tac-Toe Gibbs edition!')

# Establish and confirm player one's name
print('To begin, please input your name.')
oneName = input()
print('Player one\'s name is ' + oneName + '. Player one is X.')

# Choose between split-screen or computer opponent
print ('\nWhat type of game would you like to play?\nInput S for splitscreen.\nInput C for a computer opponent.')
selection = input()
while selection.upper() == 'S' or 'C':
  if selection.upper() == 'S':
    print ('You chose splitscreen. Good luck to both of you!')
    break

  if selection.upper() == 'C':
    print('You chose to play against the computer.\nMay the odds be ever in your favor.')
    break
  else:
    print('That is not a valid input. Please try again.')
    continue

# If applicable, establish and confirm player two's name
print('Now, what is player two\'s name?')
twoName = input()
print('Player two\'s name is ' + twoName + '. Player two is O.')

# Set up the board
one = str(1)
two = str(2)
three = str(3)
four = str(4)
five = str(5)
six = str(6)
seven = str(7)
eight = str(8)
nine = str(9)

def postBoard():
  print(oneName + ', input a number to choose a move.')
  print('    |    |    ')
  print('  ' + one + ' |  ' + two + ' |  ' + three + ' ')
  print('----|----|----')
  print('  ' + four + ' |  ' + five + ' |  ' + six + ' ')
  print('----|----|----')
  print('  ' + seven + ' |  ' + eight + ' |  ' + nine + ' ')
  print('    |    |    ')


# First player's move
if selection.upper() == 'S':
  postBoard()
oneMove = input()
if oneMove == '1':
  one = 'X'
elif oneMove == '2':
  two = 'X'
elif oneMove == '3':
  three = 'X'
elif oneMove == '4':
  four = 'X'
elif oneMove == '5':
  five = 'X'
elif oneMove == '6':
  six = 'X'
elif oneMove == '7':
  seven = 'X'
elif oneMove == '8':
  eight = 'X'
elif oneMove == '9':
  nine = 'X'
else:
  print('Invalid input. Please select a valid move.')
postBoard()