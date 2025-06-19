def edit_distance(s1,s2,i,j):
    if j < 0 and i >= 0:
        return i+1   ## s2 got exhausted, now we have to remove remaining s1

    if i < 0 and j >= 0: ## s1 gets exhausted, empty string
        return j + 1 ## to reconvert it, we have to do j+1 insertion 
    
    if s1[i] == s2[j]:
        return edit_distance(s1,s2,i-1,j-1) ## do nothing, just go ahead
    
    else:
        insert = 1 + edit_distance(s1,s2,i,j-1)
        delete = 1 + edit_distance(s1,s2,i-1,j)
        replace = 1 + edit_distance(s1,s2,i-1,j-1)

        return min(insert,delete,replace)

def memoise(s1,s2,i,j,dp):
    if j < 0 and i >= 0:
        return i+1   ## s2 got exhausted, now we have to remove remaining s1

    if i < 0 and j >= 0: ## s1 gets exhausted, empty string
        return j + 1 ## to reconvert it, we have to do j+1 insertion 
    

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = memoise(s1,s2,i-1,j-1,dp) ## do nothing, just go ahead
        return dp[i][j]
    
    else:
        insert = 1 + edit_distance(s1,s2,i,j-1)
        delete = 1 + edit_distance(s1,s2,i-1,j)
        replace = 1 + edit_distance(s1,s2,i-1,j-1)

        dp[i][j] = min(insert,delete,replace)

        return dp[i][j]

def tabular(s1,s2):
    # base
    m,n = len(s1),len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i ## 0 based indexing

    for j in range(n+1):
        dp[0][j] = j 
    
    for i in range(1,m+1):
        for j in range(1,n+1):

            if s1[i-1] == s2[j-1]:

                dp[i][j] = dp[i-1][j-1] ## do nothing, just go ahead
            
            else:
                insert = 1 + dp[i][j-1]
                delete = 1 + dp[i-1][j]
                replace = 1 + dp[i-1][j-1]

                dp[i][j] = min(insert,delete,replace)
    
    return dp[m][n]


def space_optimal(s1, s2):
    m, n = len(s1), len(s2)

    prev = list(range(n + 1))  # base case: convert empty s1 to s2 by insertions

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        curr[0] = i  # base case: convert s1[0..i-1] to empty s2 by deletions --> see base case,curr[0] is i always 

        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]  # characters match, no operation
            else:
                insert = 1 + curr[j - 1]
                delete = 1 + prev[j]
                replace = 1 + prev[j - 1]
                curr[j] = min(insert, delete, replace)

        prev = curr

    return prev[n]
