def wildcard(s1,s2,i,j):  ## s1 is first string(i) that can have */?
    # base 
    if i < 0 and j >= 0:
        return False ## s1 got exhausted

    if j < 0 and i>=0: ## s2 exhaisted, but check if s1 has all star

        for idx in range(i):
            if s1[idx] != '*':
                return False

        return True
    
    if i < 0 and j < 0: ## both exhausted
        return True


    if s1[i] == s2[j] or s1[i] == '?': ## same 
        return wildcard(s1,s2,i-1,j-1)

    else: ## not match or * present
        if s1[i] == '*': # its a star so two possible, either take s2[j] in star or dont consider
            return wildcard(s1,s2,i-1,j) or wildcard(s1,s2,i,j-1) # case 1 is * represent nothing currently, case 2 is it means that letter
        else:
            return False


def memoise(s1,s2,i,j,dp):  ## s1 is first string(i) that can have */?
    # base 
    if i < 0 and j >= 0:
        return False ## s1 got exhausted

    if j < 0 and i>=0: ## s2 exhaisted, but check if s1 has all star

        for idx in range(i+1):
            if s1[idx] != '*':
                return False

        return True
    
    if i < 0 and j < 0: ## both exhausted
        return True


    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j] or s1[i] == '?': ## same 
        dp[i][j] = memoise(s1,s2,i-1,j-1)
        return dp[i][j]

    else: ## not match or * present
        if s1[i] == '*': # its a star so two possible, either take s2[j] in star or dont consider
            dp[i][j] = memoise(s1,s2,i-1,j) or memoise(s1,s2,i,j-1) # case 1 is * represent nothing currently, case 2 is it means that letter
            return dp[i][j]

        else:
            dp[i][j] = False
            return dp[i][j]

def tabular(s1,s2):
    m,n = len(s1),len(s2)
    dp = [[False for _ in range(n+1)] for _ in range(m+1)]

    ## base
    for j in range(1,n+1): # i=0, j>0
        dp[0][j] = False

    for i in range(1,m+1): ## i>0
        flag = True
        for idx in range(1,m+1): # if even single not star, False
            if s1[idx] != '*':
                flag = False  ## j == 0
                break

        dp[i][0] = flag
    

    dp[0][0] = True

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1] or s1[i-1] == '?': ## same 

                dp[i][j] = dp[i-1][j-1]

            else: ## not match or * present
                if s1[i-1] == '*': # its a star so two possible, either take s2[j] in star or dont consider
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] # case 1 is * represent nothing currently, case 2 is it means that letter

                else:
                    dp[i][j] = False
    
    return dp[m][n]
