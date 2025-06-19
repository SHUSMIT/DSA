def single_number2(arr):
    arr.sort()
    i = 1
    while i < n:
        if arr[i] ^ arr[i-1] == 1:
            return arr[i-1]
        
        i += 3 # go 3 ahead
    
    return arr[-1] # last one