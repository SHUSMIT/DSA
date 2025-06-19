def sum_substring_first(arr,sub_str,idx,k,s): #given, substring, idx_curr, k_given, s_varaible_sum
    if idx == len(arr):
        #condition
        if k == s:  # Check if the current sum matches the target  # Print the valid subset
            return 1
        return 0
    
    sub_str.append(arr[idx]) #take
    s += arr[idx] #sum_take
    
    l = sum_substring_first(arr,sub_str,idx+1,k,s) #add all recursive call for 1st one (l)
    
    sub_str.pop() #dont take
    s-= arr[idx] #remove that
    
    r = sum_substring_first(arr,sub_str,idx+1,k,s)  #add all recursive call for 2nd one (r)
    return l+r

    
arr = [3,2,1,5,7,9,10,1,2,3,4]
k = 4
print(sum_substring_first(arr,[],0,k,0))