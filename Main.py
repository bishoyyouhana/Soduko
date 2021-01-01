#soduko game using backtracking 
#Bishoy Youhana 12/29/2020

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") 

def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve_board(board):
    #print_board(board)  debugging purposes
    #print("\n")
    emptyCell = find_empty_cell(board)
    if not emptyCell:
        return True 
    else:
        row, col = emptyCell
    
    #try possibilities out
    for i in range(1,10):
        if optionWorks(board, i, (row,col)):
            board[row][col]=i

            #recursive approach .. keeps solving everything
            if solve_board(board):
                return True

            #performs the backtrack, goes over unsolved stuff
            board[row][col] = 0

    return False

#checks if the number works 
def optionWorks(board, num, pos):
    # Check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the bog box itself
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

print_board(board)

solve_board(board)

print("\nSOLVED:\n")


print_board(board)

        