def subset_sum(arr,idx,ans,s):
    if idx == len(arr):  #reached end
        ans.append(s)  #add the current sum
        return
    
    ### not target so need of if condition
    s+= arr[idx] #add to sum
    subset_sum(arr,idx+1,ans,s) #take
    s-=arr[idx] #remove from sum
    subset_sum(arr,idx+1,ans,s) #not take
    
