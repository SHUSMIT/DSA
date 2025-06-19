def celebrity(mat):
    n = len(mat)
    top = 0
    end = n-1
    
    while top < end:

        if mat[top][end] == 1: # top knows, cant be
            top += 1
        elif mat[end][top] == 1: # end knows top, cant be
            end -= 1
        
        else: #top,end and end,top both 0 
            end -= 1
            top += 1
        
    if top > end:
        return -1
    
    else:
        for i in range(n):
            if mat[top][i] != 0: ## all row val should be 0
                return -1
            if i != top and mat[i][top] != 1: # if i != top/diagonal then all col val should be 1
                return -1
    
    return top