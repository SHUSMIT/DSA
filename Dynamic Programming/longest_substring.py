def substring_table(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] ## we actaully add the diagonal before to it
            else:
                dp[i][j] = 0 # if not equal its 0
    
    return max(max(row) for row in dp)

def space_optimal(s1,s2):
    m,n = len(s1),len(s2)
    prev = [0 for _ in range(n+1)]
    
    for i in range(1,m+1):
        curr = [0 for _ in range(n+1)]
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1] ## we actaully add the diagonal before to it
            else:
                curr[j] = 0 # if not equal its 0
        prev = curr
    
    return max(prev)

def print_substring(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    ## i need to keep track of end position of s1 = [- ,- ,- ,- ,- ]
    length = 0
    end_pos = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] ## we actaully add the diagonal before to it
                
                if dp[i][j] >= length: 
                    length = dp[i][j] ## update the length
                    end_pos = i ## keep record of ith index
                    
            else:
                dp[i][j] = 0 # if not equal its 0
    
    return s1[end_pos-length:end_pos]
    
