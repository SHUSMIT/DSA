def sub_arr_k(arr,k):
    return sub_arr_less_k(arr,k) - sub_arr_less_k(arr,k-1)


def sub_arr_less_k(arr,k): ## k is disctinct, size of map
    number = 0
    l,r = 0,0
    n = len(arr)
    map_dict = dict()

    while r < n:

        if arr[r] not in map_dict:
            map_dict[arr[r]] = 1
        else:
            map_dict[arr[r]] += 1 # store the frequency

        while len(map_dict) > k: # invalid

            map_dict[arr[l]] -= 1
            if map_dict[arr[l]] == 0:
                del(map_dict[arr[l]])
            
            l += 1 # expand
        
        length = r-l+1  # this accounts for all sub array with less than k distinct including itself
        number += length
    
    return number
