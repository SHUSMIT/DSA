def cherry_3d(i,j1,j2,a):
    ## as starting give, we use that as base 
    ## (i1,j1) and (i2,j2)
    n,m = len(a),len(a[0])
    ## both goes down so i1 = i2 = i
    if j1 < 0 or j2 < 0 or j1 >= m or j2 >=m:
        return 0
    
    if i == n-1: ## end reached
        if j1 == j2:
            return a[i][j1]
        return a[i][j1] + a[i][j2] ## different destination
    
    # for every bob move, 3 other possible for alice
    maxi = 0
    dj = [-1,0,1]
    for del1 in dj:
        for del2 in dj:
                next_col = cherry_3d(i+1,j1+del1,j2+del2) ## assumes all 9 combinations
                
            if j1+del1 == j2+del2: ## both same
                curr = a[i][j1] +  next_col
            else:
                curr = a[i][j1] + a[i][j2] + next_col
                
            maxi = max(maxi,curr) ##need the max value
    
    return maxi

def memoise(i,j1,j2,a,dp):
    ## as starting give, we use that as base 
    ## (i1,j1) and (i2,j2)
    n,m = len(a),len(a[0])
    ## both goes down so i1 = i2 = i
    if j1 < 0 or j2 < 0 or j1 >= m or j2 >=m:
        return 0
    
    if i == n-1: ## end reached
        if j1 == j2:
            return a[i][j1] ## same 
        return a[i][j1] + a[i][j2] ## different destination
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    # for every bob move, 3 other possible for alice
    dj = [-1,0,1]
    for del1 in dj:
        for del2 in dj:
            
            next_col = memoise(i+1,j1+del1,j2+del2,dp) ## assumes all 9 combinations
                
            if j1+del1 == j2+del2: ## both same
                curr = a[i][j1] +  next_col
            else:
                curr = a[i][j1] + a[i][j2] + next_col
                
            dp[i][j1][j2] = max(maxi,curr) ##need the max value
    
    return dp[i][j1][j2]

def tabulation(a):
    n, m = len(a), len(a[0])
    # dp[i][j1][j2] represents max cherries collected starting from row i, columns j1 and j2
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
    
    # Base case: last row
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n-1][j1][j2] = a[n-1][j1]
            else:
                dp[n-1][j1][j2] = a[n-1][j1] + a[n-1][j2]
    
    # Fill the DP table from bottom to top
    for i in range(n-2, -1, -1):  # from n-2 down to 0
        for j1 in range(m):
            for j2 in range(m):
                
                maxi = float('-inf')
                
                for del1 in [-1, 0, 1]:
                    for del2 in [-1, 0, 1]:
                        
                        nj1, nj2 = j1 + del1, j2 + del2
                        
                        if 0 <= nj1 < m and 0 <= nj2 < m:
                            value = dp[i+1][nj1][nj2]
                        else:
                            value = float('-inf')
                        if j1 == j2:
                            curr = a[i][j1] + value
                        else:
                            curr = a[i][j1] + a[i][j2] + value
                        maxi = max(maxi, curr)
                dp[i][j1][j2] = maxi
                
    return dp[0][0][m-1]
    
## front = dp[i]
## curr is made

def space_optimse(a):
    n, m = len(a), len(a[0])
    # dp[i][j1][j2] represents max cherries collected starting from row i, columns j1 and j2
    front = [[0 for _ in range(m)] for _ in range(m)]

    
    # Base case: last row
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = a[n-1][j1]
            else:
                front[j1][j2] = a[n-1][j1] + a[n-1][j2]
    
    # Fill the DP table from bottom to top
    for i in range(n-2, -1, -1):  # from n-2 down to 0
        
        curr = [[0 for _ in range(m)] for _ in range(m)]
        
        for j1 in range(m):
            for j2 in range(m):
                
                maxi = float('-inf')
                
                for del1 in [-1, 0, 1]:
                    for del2 in [-1, 0, 1]:
                        
                        nj1, nj2 = j1 + del1, j2 + del2
                        
                        if 0 <= nj1 < m and 0 <= nj2 < m:
                            value = front[nj1][nj2]
                        else:
                            value = float('-inf')
                        if j1 == j2:
                            curr = a[i][j1] + value
                        else:
                            curr = a[i][j1] + a[i][j2] + value
                        maxi = max(maxi, curr)
                        
                curr[j1][j2] = maxi
        
        front = cur
                
    return front[0][m-1]
