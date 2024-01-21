def calculatePosition(board, placeToPerform):
    length_board = len(board)
    x_position = placeToPerform//length_board
    y_position = placeToPerform%length_board
    return x_position, y_position

def spaceOccupied(board, x_coordinate, y_coordinate):
    if board[x_coordinate][y_coordinate] != 0:
        return True
    else:
        return False
    
def performChance(board, currentChance, placeToPerform):
    x_coordinate, y_coordinate = calculatePosition(board, placeToPerform)
    if currentChance % 2 == 0:
        board[x_coordinate][y_coordinate] = 'x'
    else:
        board[x_coordinate][y_coordinate] = 'o'

def printBoard(board):
    for i_index, row in enumerate(board):
        for j_index, element in enumerate(row):
            if j_index == len(row) - 1:
                print(element)
            else:
                print(element, end="|")
        if i_index == len(board)-1:
            print(" | | ")
        else:
            print("_|_|_")

def whoWon(board):
    i = 0
    while i < len(board):
        if board[i][0] == 'x' and board[i][1] == 'x' and board[i][2] == 'x':
            return True, 'x'
        elif board[i][0] == 'o' and board[i][1] == 'o' and board[i][2] == 'o':
            return True, 'o'
        i = i + 1
    j = 0
    while j < len(board):
        if board[0][j] == 'x' and board[1][j] == 'x' and board[2][j] == 'x':
            return True, 'x'
        elif board[0][j] == 'o' and board[1][j] == 'o' and board[2][j] == 'o':
            return True, 'o'
        j = j + 1
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        return True, 'x'
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        return True, 'x'
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        return True, 'o'
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        return True, 'o'
    return False, 0
              
def isGameOver(board, currentChance):
    output, playerWon = whoWon(board)
    if output==False:
        if currentChance > 8:
            return True, 'draw'
        else:
            return False
    else:
        return output, playerWon
    

board = [[0, 0, 0], [0, 0, 0],[0,  0,  0] ]
currentChance = 0
if currentChance<10:
    gameOver = False
    while gameOver == False:
        if currentChance<9:
            if currentChance%2==0:
                playerChance = 'x'
            else:
                playerChance = 'o'
            placeToPerform = int(input(str(playerChance )+ " Please choose a position to perform your turn"))-1
            performChance(board, currentChance, placeToPerform)
            printBoard(board)
            gameOver = isGameOver(board, currentChance)
            if gameOver==False:
                currentChance = currentChance + 1
            else:
                gameOver, playerWon = isGameOver(board, currentChance)
        else:
            playerWon ='draw'
            break    
    if playerWon == 'draw':
        print("The game was a draw!")
    else:
        print(playerWon,' won the game! Congrats!')
    
        
        
    
    currentChance = currentChance + 1



