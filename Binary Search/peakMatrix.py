def maxElement(mat,mid):
    m,n = len(mat),len(mat[0])
    maxi = float('-inf') 
    
    for i in range(m):
        if (mat[i][mid] >= maxi):
            index = i
            maxi = arr[i][mid]
            
    return index
    
def peak(mat):
    low,high = 0, len(mat[0])
    while low<=high:
        mid = (low+high)//2
        
        row = maxElement(mat,mid)
        
        left = mat[row][mid-1] if mid-1>=0 else -1
        right = mat[row][mid+1] if mid+1<len(mat[0]) else -1
        
        if mat[row][mid] > left and mat[row][mid] > right:
            return mat[row][mid]
        elif mat[row][mid] < left:
            high = mid -1
        else:
            low = mid + 1
    return -1
            