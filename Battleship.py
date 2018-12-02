from random import randint

board = []  #Initializing List board as empty list

for x in range(0, 5):
  board.append(["O"] * 5) #Make a Board(Matrix) of 5*5

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(1, len(board) )
     # Generate a random value for  row
def random_col(board):
  return randint(1, len(board) )
    # Generate a random value for col

ship_row = random_row(board)
     #Store that random value in the Variable ship_row

ship_col = random_col(board) 
      #Store that random value in the Variable ship_col

print (ship_row)
#printing it to look at the random value.

print (ship_col)
#printing it to look at the random value. 

#For Playing GAME just comment these above two lines of print

ship_row-=1
ship_col-=1

# Everything from here on should be in your for loop
# don't forget to properly indent!

for turn in range(4):
  print ("Turn", turn + 1)
  
       #Guess the row as same as of ship_row(random value) to win the Battleship
  guess_row = int(input("Guess Row: "))
  
       #Guess the col as same as of ship_col(random value) to win the Battleship
  guess_col = int(input("Guess Col: "))
     

  guess_row-=1 
  guess_col-=1 
#Decresing by -1 both the values so as it is reflected in matrix  

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    break #You win the game and it just came out of the loop
  
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
      
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      
    if (turn == 3):
      print ("Game Over")
      break
    print_board(board)
