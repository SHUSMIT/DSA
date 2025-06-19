def lcs(s1,s2):  ## need not be continuos, just longest palindromme
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] ## go diagonally, matched
                
            else: 
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1]) ## max of left,right
                
    return dp[m][n]
    
def min_insertion_palindromme(s):
    return len(s) - lcs(s,s[::-1])
    