def sum_substring(arr,sub_str,idx,k,s): #given, substring, idx_curr, k_given, s_varaible_sum
    if idx == len(arr):
        if k == s:  # Check if the current sum matches the target
            print(*sub_str)  # Print the valid subset
        return
    
    sub_str.append(arr[idx]) #take
    s += arr[idx] #sum_take
    sum_substring(arr,sub_str,idx+1,k,s) 
    sub_str.pop() #dont take
    s-= arr[idx] #remove that
    sum_substring(arr,sub_str,idx+1,k,s)

    
arr = [3,2,1,5,7,9,10,1,2,3,4]
k = 4
sum_substring(arr,[],0,k,0)