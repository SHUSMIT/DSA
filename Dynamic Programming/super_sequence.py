def lcs(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]: # equal
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    
    return dp ## the dp table

def print_lcs(s1,s2):
    m,n = len(s1),len(s2)
    dp = lcs(s1,s2)
    
    i,j = m,n
    ans = ''
    while i and j:
        if s1[i-1] == s2[j-1]: # same
            ans += s1[i-1] 
            i -= 1
            j -= 1
            
        elif dp[i-1][j] >= dp[i][j-1]: ## left big than top, go left
            
            ans += s1[i-1] ## we go left so add the opp string
            i = i - 1 
        else:
            ans += s2[j-1]
            j = j - 1
            
    if i != 0: # s1 has something
        ans += s1[0]
    if j != 0:
        ans += s2[0]
    
    return ans[::-1],dp[m][n]

def superstring(s1,s2):
    m,n = len(s1),len(s2)
    string,length = print_lcs(s1,s2)
    print('String is ' + string)
    print('length is ' + str(m + n - length) )
        
superstring('brute','groot')
    
    
    
