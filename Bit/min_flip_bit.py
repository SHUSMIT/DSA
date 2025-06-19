def min_flip_bit(start,end):
    ans = start ^ end
    count = 0
    
    for i in range(32):
        if ans & (i<<1): # this tells if ith bit is 1 or not
            count += 1
    
    return count