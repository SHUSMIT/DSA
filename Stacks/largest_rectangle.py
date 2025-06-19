def largest_rectangle(arr):
    n = len(arr)
    # store the left boundary and right boundary
    # lb -> next smaller left
    # rb -> next smaller right

    # right boundary 
    # width = r-l-1 
    st = []

    right = [n for _ in range(n)]
    for i in range(n-1,-1,-1):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        
        if st:
            right[i] = st[-1]
        
        st.append(i) # add to stack the index

    #left boundary
    st = []
    left = [-1 for _ in range(n)]
    for i in range(n):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        
        if st:
            left[i] = st[-1]
        
        st.append(i) 

    maxi = 0
    for i in range(n):
            maxi = max(maxi, arr[i] * (right[i] - left[i] - 1))

    return maxi
