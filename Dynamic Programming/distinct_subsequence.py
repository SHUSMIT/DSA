def distinct_subsequnece(s1,s2,i,j):
    if i < 0 and j >= 0: # still something of s2 is left to be matched
        return 0
    if j < 0:
        return 1 ## found combination
    
    if s1[i] == s2[j]: #it matched
        consider = distinct_subsequnece(s1,s2,i-1,j-1) ## we consider that of s1
        not_consider = distinct_subsequnece(s1,s2,i-1,j) ## we dont consider and check for more possible
        return consider + not_consider
    
    else:
        return distinct_subsequnece(s1,s2,i-1,j) ## keep searching

def memoise(s1,s2,i,j,dp):
    if i < 0 and j >= 0: # still something of s2 is left to be matched
        return 0
    if j < 0:
        return 1 ## found combination
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s1[i] == s2[j]: #it matched
        consider = memoise(s1,s2,i-1,j-1,dp) ## we consider that of s1
        not_consider = memoise(s1,s2,i-1,j,dp) ## we dont consider and check for more possible
        dp[i][j] = consider + not_consider
        return dp[i][j]
    
    else:
        dp[i][j] = memoise(s1,s2,i-1,j) ## keep searching
        return dp[i][j]

def tabular(s1,s2):
    ## we went from m,n to 0,0 .. now opp
    ## base, since -1 used, shift +1 
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1): # if j == 0 (-1 actaully, return 1)
        dp[i][0] = 1
    
    for i in range(1,m+1):
        for j in range(1,n+1):

            if s1[i-1] == s2[j-1]: #it matched
                consider = dp[i-1][j-1] ## we consider that of s1
                not_consider = dp[i-1][j] ## we dont consider and check for more possible
                dp[i][j] = consider + not_consider

            
            else:
                dp[i][j] = dp[i-1][j] ## keep searching
                
    return dp[m][n]

def space_optimal(s1,s2):
    m,n = len(s1),len(s2)
    temp = [0 for _ in range(n+1)]

    for i in range(m+1): # if j == 0 (-1 actaully, return 1)
        temp[0] = 1
    
    for i in range(1,m+1):
        curr = [0 for _ in range(n+1) ]
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]: #it matched
                consider = temp[j-1] ## we consider that of s1
                not_consider = temp[j] ## we dont consider and check for more possible

                curr[j] = consider + not_consider

            
            else:
                curr[j] = temp[j] ## keep searching

        temp = curr

    return temp[n]
    
        