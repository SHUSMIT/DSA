def grid_unique(row,col):
    if (row,col) == (0,0):
        return 1
    if row <0 or col <0: ## outside grid
        return 0
    
    up_dir = grid_unique(row-1,col)
    left_dir = grid_unique(row,col-1) ## at every case, we can do left,up 
    
    return up_dir+left_dir

def memoise(row,col,dp):
    if (row,col) == (0,0):
        return 1
    if row <0 or col <0: ## outside grid
        return 0
    if dp[row][col] != -1:
        return dp[row][col]
    
    up_dir = memoise(row-1,col,dp)
    left_dir = memoise(row,col-1.dp) ## at every case, we can do left,up 
    
    dp[row][col] = up_dir+left_dir
    
    return dp[row][col]

def tabular(row,col,dp): ## down_direction
    ##base case first
    dp[0][0] = 1
    for row in range(1,m):
        for col in range(1,n):
            up,down = 0,0
            if row > 0:
                up = dp[row-1][col]
            if col > 0:
                left = dp[row][col-1]
            dp[row][col] = up+left
    
    return dp[m-1][n-1]                
                
                
    