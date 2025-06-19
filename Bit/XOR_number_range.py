def XOR_number(N):
    
    """
    Returns XOR of all numbers from 1 to N.
    Pattern:
        N % 4 == 0 --> N
        N % 4 == 1 --> 1
        N % 4 == 2 --> N + 1
        N % 4 == 3 --> 0
    """
    
    if N % 4 == 1:
        return 1
    elif N%4 == 2:
        return N+1
    elif N%4 == 3:
        return 0
    else:
        return N

def XOR_range(a,b):
    return XOR_number(a-1) ^ XOR_number(b) 