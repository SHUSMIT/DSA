def max_sum_matrix_path(mat):
    maxi = 0
    m = len(mat)
    n = len(mat[0])
    
    for i in range(n):
        curr = recursive(m-1,i,mat) ## go for all possible values in the bottom row
        maxi = max(maxi,curr)
    return maxi
        
    
def recursive(i,j,mat):
    m = len(mat)
    n = len(mat[0])
    
    if i < 0 or j < 0 or i >= m or j >=n:
        return float('-inf') ## impossible path, so return 
    
    if i == 0:
        return mat[i][j] ## if top reached return that
    
    up = mat[i][j] + recursive(i-1,j,mat)
    up_left = mat[i][j] + recursive(i-1,j-1,mat)
    up_right = mat[i][j] + recursive(i-1,j+1,mat)
    
    return max(up,up_left,up_right)
    
def memoise(i,j,mat,dp):
    m = len(mat)
    n = len(mat[0])
    
    if i < 0 or j < 0 or i >= m or j >=n:
        return float('-inf') ## impossible path, so return 
    
    if i == 0:
        return mat[i][j] ## if base reached return that
    
    if dp[i][j] != -1:
        return dp[i][j] ## if memoized return that
    
    up = mat[i][j] + memoise(i-1,j,mat)
    up_left = mat[i][j] + memoise(i-1,j-1,mat)
    up_right = mat[i][j] + memoise(i-1,j+1,mat)
    
    dp[i][j] = max(up,up_left,up_right)
    
    return dp[i][j]
    
## the above one was top down and backtrack from up 
## tabulation is top done now go down
def tabulation(mat):
    m,n = len(mat) , len(mat[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    ## now base case, top to be filled
    for i in range(n):
        dp[0][i] = mat[0][i] ## base filled
    
    for i in range(1,m): ## i = 0 calulated above
        for j in range(n):
            
            up = mat[i][j] + dp[i-1][j]

            up_left = mat[i][j] + (dp[i - 1][j - 1] if j > 0 else float('-inf'))
            up_right = mat[i][j] + (dp[i - 1][j + 1] if j < n - 1 else float('-inf'))
            
            dp[i][j] = max(up, up_left, up_right)
            
    return max(dp[m-1])

def space_optimal(mat):
    m,n = len(mat) , len(mat[0])
    ## prev is dp[i] 
    ## curr is at end, curr[j] is basically filled, all values of of current row
    prev = mat[0][:]
    
    for i in range(1,m):
    
        curr = [0 for _ in range(n)]
        
        for j in range(n):
            up = mat[i][j] + prev[j]

            up_left = mat[i][j] + (prev[j - 1] if j > 0 else float('-inf'))
            up_right = mat[i][j] + (prev[j + 1] if j < n - 1 else float('-inf'))
            
            curr[j] = max(up, up_left, up_right)
        
        ## once curr is computed
        prev = curr[:]
    
    return max(prev)            
    
    
    

    