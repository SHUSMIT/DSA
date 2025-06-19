def min_triangle_cost(i,j,mat):
    n = len(mat)
    if i == n-1:
        return mat[n-1][j] ## return the final row val
    
    down = mat[i][j] + min_triangle_cost(i+1,j,mat)
    diagonal = mat[i][j] + min_triangle_cost(i+1,j+1,mat)
    
    ## need the minimum sum path to reach bottom
    return min(down,diagonal)

def memoize(i,j,mat,dp):
    n = len(mat)
    if i == n-1:
        return mat[n-1][j] ## return the final row val
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    down = mat[i][j] + memoize(i+1,j,mat,dp)
    diag = mat[i][j] + memoize(i+1,j+1,mat,dp)
    dp[i][j] = min(down,diag)
    return dp[i][j]

def tabulation(mat):

    n = len(mat)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[n-1][i] = mat[n-1][i] ## fill the bottom/edge case abd then build upon it
    
    for i in range(n-2,-1,-1): # start from n-2 go to 0 with decrement 1, n-1 already calulated
        for j in range(i,-1,-1):
            diag = mat[i][j] + dp[i+1][j] 
            up = mat[i][j] + dp[i+1][j+1]
            
            dp[i][j] = min(up,diag)
            
    return dp[0][0]

def space_optimal(mat):
    n = len(mat)
    temp = list()
    
    ##calulate the base,bottom
    temp[i] = mat[n-1][:] 
        
    # now go over, temp and curr, exchanging
    # temp is arr[n-1] 
    
    for i in range(n-2,-1,-1): # go up, row decrease
        # create a cur row instead of dp
        cur = [0 for _ in range(i+1)]
        
        for j in range(i+1,-1,-1):
            
        up = mat[i][j] + temp[j] ## go up
        diag = mat[i][j] + temp[j+1] # go diagonal
        
        cur[j] = min(up,diag) ## calulate the row
    
    # once the entire for loop is creates the cur
    temp = cur[:] 
    
    return temp[0]
    
    
    