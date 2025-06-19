def sub_string(arr,target,idx,ds,ans):
    if idx==len(arr):
        if target ==0: ## target gets reduced to 0
            ans.append(ds[:])  #deep copy added
        return


    if arr[idx] <= target:
        ds.append(arr[idx]) ##add that element to the substring
        sub_string(arr,target-arr[idx],idx+1,ds,ans)  #here +1 done so that no repeat of same idx done
        ds.pop() #remove the last added

    while idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:  
        idx += 1

    sub_string(arr,target, idx+1, ds, ans)

        


ans = []
candidates.sort()
sub_string(candidates,target,0,[],ans)
print(ans)