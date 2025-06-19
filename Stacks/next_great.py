def next_greater(arr):
    n = len(arr)
    st = []
    ans = [-1 for i in range(n)]
    st.append(arr)

    for i in range(n-2,-1,-1):

        while st and st[-1] <= arr[i]:
            st.pop() # keep popping till the top elelemnt exist or smaller equal to a[i]
        
        if st: # now if isnt empty, that is the ans
            ans[i] = st[-1] # the top
            st.append(arr[i]) # and add it to the stack

        else:
            st.append(arr[i])  # sttil ladd to stack, by default all is -1
    
    return ans


    