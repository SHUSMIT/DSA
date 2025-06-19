arr.insert(0,1)
arr.append(1)

##required for extreme, i=1, j =n initially

def baloon(i,j,arr):
    if i > j:
        return 0
    
    maxi = float('-inf')

    for idx in range(i,j+1):
        cost = arr[i-1] * arr[idx] * arr[j+1] + baloon(i,idx-1,arr) + baloon(idx+1,j,arr) ## from bottom to up

        maxi = max(maxi,cost)
    
    return maxi