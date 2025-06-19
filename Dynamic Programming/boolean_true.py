def boolean_true(i, j, isTrue, arr):
    if i == j:
        if isTrue == 1: ## true needed
            return 1 if arr[i] == 'T' else 0
        else: #false req
            return 1 if arr[i] == 'F' else 0

    ways = 0  ## compute all ways when false when true as we are breaking into sub problems

    for idx in range(i + 1, j, 2): # i+1 to j-1

        operator = arr[idx] 

        lt = boolean_true(i, idx - 1, 1, arr)
        lf = boolean_true(i, idx - 1, 0, arr)
        rt = boolean_true(idx + 1, j, 1, arr)
        rf = boolean_true(idx + 1, j, 0, arr)

        if operator == '&':
            if isTrue:  # to get true and
                ways += lt * rt
            else: # to get false and
                ways += lt * rf + lf * rt + lf * rf

        elif operator == '|':
            if isTrue:
                ways += lt * rt + lt * rf + lf * rt
            else:
                ways += lf * rf

        elif operator == '^':
            if isTrue:
                ways += lt * rf + lf * rt
            else:
                ways += lt * rt + lf * rf

    return ways

def memoise(i, j, isTrue, arr,dp):
    
    if i == j:
        if isTrue == 1: ## true needed
            return 1 if arr[i] == 'T' else 0
        else: #false req
            return 1 if arr[i] == 'F' else 0


    if dp[i][j][isTrue] != -1:
        return dp[i][j][isTrue]

    ways = 0  ## compute all ways when false when true as we are breaking into sub problems

    for idx in range(i + 1, j, 2): # i+1 to j-1

        operator = arr[idx] 

        lt = memoise(i, idx - 1, 1, arr,dp)
        lf = memoise(i, idx - 1, 0, arr,dp)
        rt = memoise(idx + 1, j, 1, arr,dp)
        rf = memoise(idx + 1, j, 0, arr,dp)

        if operator == '&':
            if isTrue:  # to get true and
                ways += lt * rt
            else: # to get false and
                ways += lt * rf + lf * rt + lf * rf

        elif operator == '|':
            if isTrue:
                ways += lt * rt + lt * rf + lf * rt
            else:
                ways += lf * rf

        elif operator == '^':
            if isTrue:
                ways += lt * rf + lf * rt
            else:
                ways += lt * rt + lf * rf

    dp[i][j][isTrue] = ways

    return dp[i][j][isTrue]

