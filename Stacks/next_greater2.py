def next_great2(arr):
    # go from 2N-1 towarda (double it) and i%N to get the val duplicated from arr
    # follow same 

    n = len(arr)
    st = []
    ans = [-1 for i in range(n)]

    st.append(arr[-1]) # add the last, ie, 2n-1
    for i in range(2*n-2, -1, -1):

        while st and st[-1] <= arr[ i%n ]:
            st.pop()
        
        if st:
            ans[i % n] = st[-1]  # just overwrite the values -- > i % n rather than i
            st.append(arr[i%n])
        else:
            st.append(arr[i%n])
    
    return ans


