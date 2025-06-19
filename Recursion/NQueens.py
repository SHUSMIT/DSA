def isFill(row,col,board,n):
    dr,dc = row,col ## copy it as we modify it
    
    ##upper diagonal check 
    while(row >= 0 and col >= 0):  ## till upper and lower border reached
        if(board[row][col] == 'Q'):
            return False
        row -= 1
        col -= 1
    
    ## check sideway where col constant, row decrease
    row,col = dr,dc
    
    while(col>=0):
        if(board[row][col] == 'Q'):
            return False
        
        col -= 1
    
    
    ## check the lower diagonal now 
    row,col = dr,dc
    
    while(row < n and col >= 0):
        if(board[row][col] == 'Q'):
            return False
        
        row += 1
        col -= 1
    
    return True

def solve(col,board,ans,n):
    if col == n:   ## if col index reaches the last index/board
        ans.append([''.join(row) for row in board])  ## store the board in answer ## deep copy
        return
    
    ## now we check each row where to place         
    for row in range(0,n):
        if(isFill(row,col,board,n)):
            board[row][col] = 'Q'
            solve(col+1,board,ans,n)   ## we now go to next column
            board[row][col] = '.'   ## remove the queen as  board was altered
        

n = int(input())
board = [['.' for _ in range(n)] for _ in range(n) ]
ans = list()
solve(0,board,ans,n)
print(ans)
        