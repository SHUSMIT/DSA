def next_smaller(arr):
    n = len(arr)
    ans = [-1 for i in range(n)]
    st = []
    st.append(arr[0]) # push first

    for i in range(1,n): # go from left to right as check on left side to be done
        while st and st[-1] >= arr[i]: # until its smaller
            st.pop()
        
        if st:
            ans[i] = st[-1]
            st.append(arr[i])
        else:
            st.append(arr[i])

    return ans