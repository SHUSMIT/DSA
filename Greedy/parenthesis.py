# if ( -> count ++
# if ) -> count -- 
# if * -> count can be any

def recurse_paren(idx,count,s):
    n = len(s)
    if count < 0:
        return False
    
    if idx == n-1: # end reached
        return count == 0 # 0 means all closed
    
    if s[idx] == '(':
        return recurse_paren(idx+1,count+1,s)
    elif s[idx] == ')':
        return recurse_paren(idx+1,count-1,s)
    else:
        return recurse_paren(idx+1,count,s) or recurse_paren(idx+1,count+1,s) or recurse_paren(idx+1,count-1,s) ## all 3 possible, any true, means all true

# recursive 3^n, on tabulation -> O(n^2)

def valid_parenthe(s):
    upper = 0
    lower = 0
    # keep upper and lower bound
    # * means [-1,1] is range
    # lower = 0 if negative, but upper should be 0/+ve , else break False
    
    for i in range(n):

        if s[i] == '(':
            lower += 1
            upper += 1
        elif s[i] == ')':
            lower -= 1
            upper -= 1
        else:
            lower -=1 # star means anything [-1,1]
            upper += 1
        
        if lower < 0:
            lower = 0 # make it 0 if -ve
        if upper <0: # if upper is -ve means cant be +ve again
            return False 
    
    return lower == 0 ## if lower isnt 0 by any means, it is open