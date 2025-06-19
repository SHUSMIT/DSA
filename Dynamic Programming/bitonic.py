def lis(arr):
    n = len(arr)
    dp = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                length = 1 + dp[j]
                
                dp[i] = max(dp[i],length)
    return dp

def bitonic(arr):
    n = len(arr)
    dp_forward_increase = lis(arr)
    dp_backward_increase = lis(arr[::-1])
    dp_backward_increase.reverse() ## allign indices
    bitonic = []

    for i in range(n):
        bitonic.append(dp_backward_increase[i] + dp_backward_increase[i] - 1)
    
    return max(bitonic)


def find_bitonic(arr):
    n = len(arr)
    # Increasing subsequence (LIS)
    dp1 = [1] * n
    parent1 = [-1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp1[j] + 1 > dp1[i]:
                dp1[i] = dp1[j] + 1
                parent1[i] = j

    # Decreasing subsequence (LDS)
    dp2 = [1] * n
    parent2 = [-1] * n
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dp2[j] + 1 > dp2[i]:
                dp2[i] = dp2[j] + 1
                parent2[i] = j

    # Find peak index
    max_len = 0
    peak = 0
    for i in range(n):
        if dp1[i] + dp2[i] - 1 > max_len:
            max_len = dp1[i] + dp2[i] - 1
            peak = i

    # Reconstruct increasing part (LIS up to peak)
    inc = []
    i = peak
    while i != -1:
        inc.append(arr[i])
        i = parent1[i]
    inc.reverse()

    # Reconstruct decreasing part (LDS from peak)
    dec = []
    i = parent2[peak]
    while i != -1:
        dec.append(arr[i])
        i = parent2[i]

    # Combine
    bitonic_seq = inc + dec
    return bitonic_seq