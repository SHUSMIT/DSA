def permutation_no_space(ans,idx,arr):
    if idx == len(arr):
        ans.append(arr[:]) ##depp copy
        return
    
    for i in range(idx,len(arr)):
        swap(arr,i,idx)     ###Call the swap function to swap that element(idx) with ith one ( which increments later (idx --> last))
        permutation_no_space(ans,idx+1,arr) ## move the index to the next one, recursively
        swap(arr,i,idx)  ###Call the swap function again for back tracking

def swap(arr,i,j):
    arr[i],arr[j] = arr[j] , arr[i]