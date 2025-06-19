def longest_string_k(s):
    n = len(s)
    l,r = 0,0
    maxi = float('-inf')
    string_map = {}
    l_id,r_id = 0,0

    while r < n:
        if s[r] in string_map: # present
            if string_map[s[r]] >= l: # its in required window
                l = string_map[s[r]] + 1 # update the l value
        
        string_map[s[r]] = r # update the index as not present
        length = r-l+1
        if length > maxi:
            maxi = length
            r_id = r
            l_id = l
            ## store all above
        
        r += 1 # update r always
        
    return length,s[l_id:r_id+1]
        