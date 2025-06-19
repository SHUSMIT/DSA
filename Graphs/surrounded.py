
def dfs(mat,visited,row,col,directions,m,n):
    visited[row][col] = 1
    for (dr,dc) in directions:
        r = row + dr
        c = col + dc
        if 0<=r<m and 0<=c<n:
            if not visited[r][c] and mat[r][c] == 'O':
                dfs(mat,visited,r,c,directions,m,n)


def surrounded(mat):
    #boundary means row = 0, n-1 and column 0,m-1
    m,n = len(mat),len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                if mat[i][j] == 'O' and not visited[i][j]:
                    dfs(mat,visited,i,j,directions,m,n)  ## visit all boundary
    
    altered_mat = [row[:] for row in mat]
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and altered_mat[i][j] == 'O':
                altered_mat[i][j] = 'X'
                
    return altered_mat
                
        