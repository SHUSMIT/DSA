def leaders(arr):
    n = len(arr)
    st = []
    st.append(arr[n-1])
    maxi = arr[n-1]

    for i in range(n-2,-1,-1):
        # update the current maxi
        if arr[i] > maxi: # if curr element is more than maxi, add it
            st.append(arr[i])
        
        maxi = max(maxi,arr[i]) # update the max
    
    return sorted(ans)

        