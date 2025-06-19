def lower_bound(x,arr): # element >= x
    low = 0
    high = len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1 
    
    return ans


def length_lcs_bs(arr):
    ans = list()
    n = len(arr)
    ans.append(arr[0])

    for i in range(1,n):
        if arr[i] > ans[-1]: ## current guy is greater than last added
            ans.append(arr[i])
        else: ## bs of lower bound and replace
            x = lower_bound(arr[i],ans) # find idx of lower bound of i in ans
            ans[x] = arr[i] # replace it
    
    return len(ans)


