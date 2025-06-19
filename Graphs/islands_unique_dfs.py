from collections import deque

def dfs(visited,mat,directions,row,col,m,n,list_islands,row_base,col_base):
    
    visited[row][col] = True
    list_islands.append((row-row_base , col-col_base))   ## to store the shape, subtract cur_row,col - base row,col
    
    for (dr,dc) in directions:
        r = row + dr
        c = col + dc
        if 0<=r<m and 0<=c<n:
            if not visited[r][c] and mat[r][c]:
                dfs(visited,mat,directions,r,c,m,n,list_islands,row_base,col_base)
                
                
                

def islands_distinc_dfs(mat):
    m,n = len(mat) , len(mat[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    directions = [ (-1,-1) , (-1,0) , (-1,1),
                    (0,-1) ,         (0,1),
                    (1,-1) , (1,0)  , (1,1) ]  ## all 8 direction where travel possible
    
    count = 0  
    
    unique_islands = set()
    for i in range(m):
        for j in range(n):
            
            if not visited[i][j] and mat[i][j] == 1:
                list_islands = list()  ## create a list of islands corrodinates
                dfs(visited,mat,directions,i,j,m,n,list_islands,i,j)
                unique_islands.add(tuple(list_islands))  ## use tuple to store it
                
    
    return len(unique_islands) 
