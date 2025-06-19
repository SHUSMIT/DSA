def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return (a,b)

def check_ith_bit_left(N,k):
    #left shift << 
    return (N & (1<<k))

def check_ith_bit_right(N,k):
    #right shift >> 
    return (N>>k) & 1 