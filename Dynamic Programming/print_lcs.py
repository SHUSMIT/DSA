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
    
    return dp

def print_lcs(s1,s2):
    m,n = len(s1),len(s2)
    dp = tabular(s1,s2)
    
    ## now go from (n,m) till either of it is exhausted
    ## if string matches, it came from 1+(i-1,j-1)
    # else it came from max(i-1,j-1) route -> check left and up, go towards max
    ## keep storing
    
    ans = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1]  == s2[j-1]: ## 1 based index/shifted, matched
            ans += s[i-1] #concatenate
            i = i-1 ## both move
            j = j-1 
            
        elif dp[i-1][j] <= dp[i][j-1]:  ## not equal, up is bigger than left
            j = j-1  ## go up
        else:
            i = i-1 ## go left
    
    return ans[::-1] ## reverse 
        