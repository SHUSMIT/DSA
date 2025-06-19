def unique_subsets(arr,ans,idx,sub):
    if idx == len(arr):
        ans.append(sub[:])
        return
    
    sub.append(arr[idx])
    unique_subsets(arr,ans,idx+1,sub)
    sub.pop()
    
    while idx+1 < len(arr) and arr[idx] == arr[idx+1]:
        idx += 1
    
    unique_subsets(arr,ans,idx+1,sub)

arr.sort()
ans = list()
unique_subsets(arr,ans,0,[])