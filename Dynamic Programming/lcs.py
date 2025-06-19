def lcs(idx1,idx2,s1,s2):
    
    if idx1 < 0 or idx2 < 0:
        return 0 ## longest when last idx reached
    
    if s1[idx1] == s2[idx2]:
        return 1 + lcs(idx1-1,idx2-1,s1,s2) ## matched so both move
    else:
        return max( lcs(idx1-1,idx2,s1,s2) , lcs(idx1,idx2-1,s1,s2) ) ## not matched
    
def memoise(idx1,idx2,s1,s2,dp):
    if idx1 < 0 or idx2 < 0:
        return 0 ## longest when last idx reached
    
    if dp[idx1][idx2] != -1:
        return dp[idx1][idx2]
        
    if s1[idx1] == s2[idx2]:
        dp[idx1][idx2] = 1 + memoise(idx1-1,idx2-1,s1,s2) ## matched so both move and length ++ 
        return dp[idx1][idx2]
        
    else:
        dp[idx1][idx2] = max( memoise(idx1-1,idx2,s1,s2) , memoise(idx1,idx2-1,s1,s2) ) ## not matched
        return dp[idx1][idx2]

def tabular(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1) ]
    
    ## shift by 1 and treat (i,j) as (i-1,j-1)
    ## could shift above also
    
    # for i in range(m):
    #     for j in range(n):
    #             dp[0][j] = 0 
    #             dp[i][0] = 0  ## already initiliased to 0
         
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if s1[i-1] == s2[j-1]: ## treat (i,j) as (i-1,j-1)
            
                dp[i][j] = 1 + dp[i-1][j-1] ## matched so both move and length ++ 
            
            else:
                dp[i][j] = max( dp[i-1][j] , dp[i][j-1] ) ## not matched
    
    return dp[m][n]
            