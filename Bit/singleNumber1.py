def single_number1(arr):
    xor = 0 
    for i in range(n):
        xor = xor ^ arr[i]
    
    return xor