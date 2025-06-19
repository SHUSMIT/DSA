def max_sum_subarr_kadane(arr):
    n = len(arr)
    # if sum is negative, we make it 0
    # if its positive we keep adding/going
    # maximum sum is also kep recrod of
    # start index and end index for printing
    maxi = float('-inf')
    cur_sum = 0

    for i in range(n):
        cur_sum += arr[i]
        maxi = max(maxi,cur_sum)

        if cur_sum < 0:
            cur_sum = 0
        
    return maxi if maxi > 0 else []

def print_max_subarr(arr):
    n = len(arr)

    st = -1
    ed = -1
    start = -1
    maxi = float('-inf')
    cur_sum = 0

    for i in range(n):
        if cur_sum == 0:
            start = i # index of starting as cur sum is 0

        cur_sum += arr[i]

        if cur_sum > maxi:
            maxi = max(maxi,cur_sum)
            st = start
            ed = i # end index is current index 
        
        if cur_sum<0:
            cur_sum=0
    
    return arr[st:ed+1] if maxi > 0 else {}
        
    
