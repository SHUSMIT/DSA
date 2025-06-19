def lcs(s1,s2):
    m,n = len(s1),len(s2)
    dp [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    length = 0
    end_idx = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] ## go diagonally 
                
                if length <= dp[i][j]:
                    length = dp[i][j]
                    end_idx = i
                    
            else:
                dp[i][j] = 0
                
    return s1[end_idx-length : end_idx]
    
def longest_palindromme(s):
    return lcs(s,reversed(s))