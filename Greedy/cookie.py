def assign_cookie(cookie,child):
    cookie.sort()  # l
    child.sort()  # r
    ## sort both of them
    n,m = len(cookie), len(child)
    l,r = 0,0

    while l < n and r < m: # both required to be withing bound

        if cookie[l] >= child[r]: # if cookie l satisfy child r
            r += 1
            l += 1
        else:
            l+=1  # go further as, if l cant satisfy r, it cant satisy r + 1 ... 
    
    return r+1