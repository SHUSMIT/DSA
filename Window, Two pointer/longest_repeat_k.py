def longest_repeat_k(arr,k):
    l,r = 0,0
    max_freq = 0 
    map_dict = {}
    maxi = 0
    n = len(arr)

    while r < n:
        
        if arr[r] not in map_dict:
            map_dict[arr[r]] = 1
            max_freq = max(max_freq,1)
        
        else:
            map_dict[arr[r]] += 1
            max_freq = max(max_freq,map_dict[arr[r]]) # check if it can be max frequency

        
        changes = (r-l+1) - max_freq ## that is the number of changes req to make length string into single char string

        while changes > k:  # no need to reassign max_freq as that wouldnt change the length
            map_dict[arr[l]] -= 1 # reduce
            l += 1 # move left, shrink
        

        maxi = max(maxi,r-l+1)
        r += 1
    
    return maxi

