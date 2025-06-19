def substring_3char(arr):
    l,r = 0,0
    count = 0
    last_seen = {'a':-1, 'b':-1, 'c':-1}

    while r < n:

        last_seen[arr[r]] = r # store the index of latest seen char

        if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1: # all seen once
            count += (1 + min( last_seen['a'] , last_seen['b'] , last_seen['c'])) # 1 + min(left) 
            
        r += 1
    
    return count

