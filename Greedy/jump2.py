def jump_game2_recursion(idx,jump,arr):

    if idx >= n-1:
        return jumps ## current jumps
    
    mini = float('inf')

    for i in range(1,arr[idx]+1): ## i can make that many jumps as in
        mini = min(mini, jump_game2_recursion(idx+i,jump+1,arr))
    
    return mini

def jump2_optimal(arr):
    jump = 0
    l,r = 0,0 
    n = len(arr)

    while r < n-1: # moment last idx reached or crossed
        furthest = 0
        for i in range(l,r+1): # check for furthest between l and l+r (inclusive) range

            furthest = max(furthest , i + arr[i])
        
        l = r + 1 # move l 1 ahead of r
        r = furthest # move r to furthest
        jump +=1
    
    return jump

    