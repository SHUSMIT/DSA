def three_sum(arr,target):
    n = len(arr)
    # take i first, loop j and k 
    # if sum is smaller, j ++ else k --
    # once sum got, store it.
    # keep skipping j and k if duplicate till a new no
    # j and k crossed, move i now, but keep skipping till new val if duplicate
    arr.sort()
    ans = []
    for i in range(n):

        if i > 0 and arr[i] == arr[i-1]:
            continue # skip for i also 

        j,k = i+1,n-1 # for every fixed i to this
    
        while j < k:
            
            cur_sum = arr[j] + arr[k] + arr[i]

            if cur_sum > target:
                k -= 1
            elif cur_sum < target:
                j += 1

            else: # equal            
                ans.append([arr[i],arr[j],arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j-1]:
                    j += 1 # no duplicate
                while j < k and arr[k] == arr[k-1]:
                    k -= 1

    return ans
        
        