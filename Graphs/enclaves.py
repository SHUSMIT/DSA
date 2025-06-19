
def dfs(mat,visited,row,col,directions,m,n):
    visited[row][col] = 1
    for (dr,dc) in directions:
        r = row + dr
        c = col + dc
        if 0<=r<m and 0<=c<n:
            if not visited[r][c] and mat[r][c] == 1:
                dfs(mat,visited,r,c,directions,m,n)

## 1's from where boundary reach --> count of boundary se connected only

def number_of_enclave(mat):
    #boundary means row = 0, n-1 and column 0,m-1
    m,n = len(mat),len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                if mat[i][j] == 1 and not visited[i][j]:
                    dfs(mat,visited,i,j,directions,m,n)  ## visit all boundary
    
    count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and not visited[i][j]:
                count += 1
    
                
    return count