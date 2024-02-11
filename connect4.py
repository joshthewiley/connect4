"""

GAME LOOP

1. Print board
2. User input
3. Update board
4. Check for win
5. Switch players 

"""

# Initialize Game

# IDEA: Allow for different board sizes.
# height = 6
# width = 7

board = [ [ '_' for i in range(7)] for i in range(6) ]
currPlayer = 0
symbols = ['X', 'O']

# Print Board TODO: Make prettier.
def displayBoard():
    print(' ', *[i+1 for i in range(7)], ' ')
    for row in board:
        print('|', *row, '|')

    print('_' * 17)

def getInput():
    column = 0

    while True:
        newPlay = input(f'Please enter the column of your next move (1-7): ')

        # Check that input is an integer.
        try:
            column = int(newPlay) - 1
        except:
            print('Sorry, that input was not recognized as a number.\n')
            continue

        # Check if that column exist in the board.
        if not (0 <= column < len(board[0])):
            print('Sorry, that number is not a valid column.\n')
            continue

        # Check if column is already full.
        if board[0][column] != '_':
            print('Sorry, that column is full, please choose a different one.\n')
            continue
                
        # Input seems good, lets go with it!
        break
    return column 

def updateBoard(column: int, i=0):
    if i < len(board)-1 and board[i+1][column] == '_':
        updateBoard(column, i+1)
        return
    board[i][column] = symbols[currPlayer]

def checkWin():
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell != '_':

                # Vertical from cell      [0][0] - [2][6]
                # Diagonal down from cell [0][0] - [2][3]
                if i < 3 and j < 7:
                    # Vertical
                    if cell == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                        return cell
    
                    elif j < 3:
                        # Diagonal down
                        if cell == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                            return cell

                # Horizontal from cell    [0][0] - [5][3]
                # Diagonal up from cell   [3][0] - [5][3]
                if i < 6 and j < 4:
                    # Horizontal
                    if cell == row[j+1] == row[j+2] == row[j+3]:
                        return cell 

                    elif i > 2:
                        # Diagonal up
                        if cell == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                            return cell
                        
    # Didn't find any winning configurations.
    return False


while True:
    print('')
    displayBoard()
    print('')
    print(f'Hello Player {symbols[currPlayer]}!')

    updateBoard(getInput())

    win = checkWin()
    if win:
        print('')
        displayBoard()
        print(f"\n--------------------\n\n Player {win} has won!\n\n--------------------\n")
        break

    # Switch Players
    currPlayer = 1 if currPlayer == 0 else 0
    