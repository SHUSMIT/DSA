def majority(arr):
    n= len(arr)
    freq = {}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
            continue
        freq[arr[i]] +=1
    
    req = len(arr)//2

    return len(arr)//2 < max(freq.values())

def majorit_moore(arr):
    count = 0
    val = 0

    or i in range(n):
        if count == 0:
            candidate = arr[i]
            count = 1
        elif candidate == arr[i]:  # Same element
            count += 1
        else:  # Different element
            count -= 1
    
    count = 0
    for i in range(n):
        if arr[i] == target:
            count += 1
    
    if count > len(arr)//2:
        return target
    
    return -1