def missing_repeat(arr):
    n = len(arr)
    
    S = sum(arr)
    S2 = sum(i**2 for i in arr)

    sn = n * (n+1) // 2
    sn2 = n * (2 * n + 1) * (n + 1) // 12

    #(x-y) = S - Sn
    #(x+y) = S2 - s2n / (x-y)

    diff = S - sn
    add = (S2 - sn2 ) / diff

    #repeat = x and not present = y
    x = (add+diff) // 2
    y = (add-diff) // 2

    return x,y
    


    
