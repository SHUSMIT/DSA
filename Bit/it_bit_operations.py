def set_ith(N,i):
    return N | (1<<i)

def clear_ith(N,i):
    return N & (~(1<<i))

def toggle_ith(N,i):
    return N ^ (1 << i)

def remove_last_set(N):
    return N & N-1

def is_power2(N): # since only 1 set bit, do the remval, if removed it would equal 0
    return (N & N-1) == 0