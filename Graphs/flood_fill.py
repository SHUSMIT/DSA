from collections import deque

def dfs(modified_mat,mat,directions,visited,src_r,src_c,m,n):
    visited[src_r][src_c] = 1
    modified_mat[src_r][src_c] = 2
    for (dr,dc) in directions:
        r = src_r + dr
        c = src_c + dc
        if 0<=r<m and 0<=c<n:
            if not visited[r][c] and mat[r][c] == 1:
                dfs(modified_mat,mat,directions,r,c,m,n)
        
def flood_fill_dfs(mat,src_r,src_c):
    m,n = len(mat),len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    modified_mat =[row[:] for row in mat]

    ## we keep a visited, we keep an original matrixx, we make a duplicate matrix where we do the work
    ## if visited = 0, original has 1, duplicate will be = 2
    ## if visited = 0, orginal has 0, nothing to be done. all in single pass
    
    directions = [   (-1,0),
                    (0,-1),(0,1),
                    (1,0)]
    
    dfs(modified_mat,mat,directions,visited,src_r,src_c,m,n)
    
    return modified_mat
