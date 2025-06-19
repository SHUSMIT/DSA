from collections import deque

def sliding_window(arr,k):
    dq = deque()
    n = len(arr)
    ans = []

    #i-k+1 gives index of start of window

    for i in range(n):
        if dq and dq[0] < i-k+1: # window start is now more, pop
            dq.popleft()
        
        while dq and arr[i] > arr[dq[-1]]: # the top is less , so cant contribute to max -- remove/pop
            dq.pop()
        
        dq.append(i) # it gets removed in next iteration

        if i-k+1 >= 0: # now its a valid index
            ans.append(arr[dq[0]]) #the left start of dq will have the index 
        
    return ans
            