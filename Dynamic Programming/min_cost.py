def minimial_cost(row,col,mat):
    if (row,col) == (0,0):
        return mat[0][0] ## reached base
    if row < 0 or col < 0:
        return 1e9
    
    up = mat[row][col] + minimial_cost(row-1,col,mat)
    down = mat[row][col] + minimial_cost(row,col-1,mat)
    
    return min(up,down)

def memoise(row,col,mat,dp):
    if (row,col) == (0,0):
        return mat[0][0] ## reached base
        
    if row < 0 or col < 0:
        return 1e9
        
    if dp[row][col] != -1:
        return dp[row][col]
        
    up = mat[row][col] +  memoise(row-1,col,mat,dp)
    down = mat[row][col] +  memoise(row,col-1,mat,dp)
    
    dp[row][col] = min(up,down)
    return dp[row][col]

def tabular(mat):
    dp[0][0] = mat[0][0]
    n,m = len(mat),len(mat[0])
    
    for i in range(n):
        for j in range(m):
            up = (mat[i][j] + dp[i-1][j]) if i > 0 else 1e9
            down =  (mat[i][j] + dp[i][j-1]) if j > 0 else 1e9
            
            dp[i][j] = min(up,down)
        
    return dp[n-1][m-1]
            
                
            
