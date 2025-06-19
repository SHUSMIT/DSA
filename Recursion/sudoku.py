def isValid(board,row,col,char):
    for i in range(9):
        if(board[i][col] == char or board[row][i] == char):
            return False
            
    strtRow = 3 * (row//3)
    strtCol = 3 * (col//3)
    
    for i in range(3):
        for j in range(3):
            if board[strtRow + i][strtCol + j] == char:
                return False
                
    return True
    

def solve(board):
    ##traverse the board to find the missing 
    for i in range(9): 
        for j in range(9):
            if board[i][j] == '.':
                for num in range(1,10):
                    char = str(num)  ### we will check for all number now
                    if isValid(board,i,j,char):
                        board[i][j] = char
                        if solve(board):
                            return True ## recursively go ahead
                            
                        board[i][j] = '.' ## back track if not valid found
                        
                return False
    return True ## all filled