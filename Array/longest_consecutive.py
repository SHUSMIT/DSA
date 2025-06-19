def longest_consecutive(arr):
    arr.sort()
    if len(arr) == 0:
        return -1

    cur_l = 1
    length = 1
    last = -1

    for i in arr:
        if i == last:
            continue # its the same, so skip and check for new

        elif i == last + 1: # can be a part of new seq
            cur_l += 1
            length = max(cur_l,length)
            last = i 

        elif i != last + 1:
            last = i # cannot be a part of seq so start a new seq
            cur_l = 1 # re_initialise
    
    length = max(cur_l,length)
    
    return length

def optimal(arr):

    nums_set = set(arr) # create a set ds
    length = 1

    for nums in arr: # go through ar

        if num - 1 not in nums_set: # we find the num whose prev(num-1) isnt there in set
            current = num # update to that num
            cur_length = 1 # have cur length

            while current + 1 in nums_set: # while others exist, keep updating
                cur_length += 1
                current = current + 1
            
            length = max(length,cur_length)
    
    return length
        