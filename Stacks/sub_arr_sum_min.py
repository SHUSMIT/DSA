def next_small(arr,n):
    small = [n for _ in range(n)]
    st = []


    for i in range(n-1,-1,-1):
        while st and arr[st[-1]] > arr[i]: # current top element is greater, arr[st] because we are using index i stack
            st.pop()
        
        if st:
            small[i] = st[-1] #assign the top
        
        st.append(i) # store the index of greater element rather

    return small

def previous_small(arr,n):

    small = [-1 for _ in range(n)]
    st = []

    for i in range(n):

        while st and arr[st[-1]] > arr[i]: # current top element is greater
            st.pop()
        
        if st:
            small[i] = st[-1] # assign the top
        
        st.append(i) # store the index of greater element rather

    return small


def sum_min_subarray(arr):
    n = len(arr)
    next_smaller = next_small(arr,n)
    prev_smaller = previous_small(arr,n)
    total = 0

    for i in range(n):
        total += (i-prev_smaller[i]) * (next_smaller[i] - i) * arr[i]
    
    return total