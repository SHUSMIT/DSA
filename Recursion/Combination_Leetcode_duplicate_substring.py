def sub_string(idx,target,arr,ds,ans):

    if idx == len(arr): ##End index reached
        if target ==0:  #target got reduced to 0
            ans.append(ds[:]) #add the current ds/substring by deep copy
        return

    if arr[idx] <= target:
        ds.append(arr[idx]) #add it to the ds
        sub_string(idx,target-arr[idx],arr,ds,ans) #subtract from target the current element added
        ds.pop() ##remove the last/backtracking
    
    sub_string(idx+1,target,arr,ds,ans)

