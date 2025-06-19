n = len(arr)
arr.insert(0,0)
arr.append(n)

#i =1 , j = n
##required above as 
# length = arr[i-1] - arr[j+1] , i=

def cost_cut_length(i,j,arr):

    if i > j:
        return 0

    mini = float('inf')

    for idx in range(i,j+1): #upto j
        cost = arr[j+1] - arr[i] + cost_cut_length(i,idx-1,arr) + cost_cut_length(idx+1,j,arr)
        mini = min(mini,cost)

    return mini