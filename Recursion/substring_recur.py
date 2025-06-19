def substring(idx,arr,sub_arr):
    if (idx == len(arr)):
        print(*sub_arr)
        return
         
    sub_arr.append(arr[idx])  #Add it ( -> )
    substring(idx+1,arr,sub_arr) #Take
    
    sub_arr.pop() #Remove the last added to substring( <- )
    substring(idx+1,arr,sub_arr) #Don't take
    
arr = [3,2,1]
substring(0,arr,[])           