def swap_arr(arr,i,n):
    if i >= n/2:
        return
    
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]  #swap them
    
    swap_arr(arr,i+1,len(arr))

arr = [1,4,5,6,7,7,8,9,10,11]

print(arr)
swap_arr(arr,0,len(arr))
print(arr)