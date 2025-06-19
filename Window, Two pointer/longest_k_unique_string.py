def longest_string_k_char(s,k):
    l,r = 0,0
    freq_dict = dict()
    maxi = 0
    n = len(arr)
    
    while r < n:

        if s[r] not in freq_dict:
            freq_dict[s[r]] = 1
        else: 
            freq_dict[s[r]] += 1
        
        while len(freq_dict) > k:
            freq_dict[s[l]] -= 1

            if freq_dict[s[l]] == 0:
                del(freq_dict[s[l]])
            
            l += 1 # keep shrinking
        
        maxi = max(maxi,r-l+1)
        r += 1
    
    return maxi
