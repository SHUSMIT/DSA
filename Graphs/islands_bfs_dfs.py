from collections import deque

def dfs(visited,mat,directions,row,col,m,n):
    visited[row][col] = True
    for (dr,dc) in directions:
        r = row + dr
        c = col + dc
        if 0<=r<m and 0<=c<n:
            if not visited[r][c] and mat[r][c]:
                dfs(visited,mat,directions,r,c,m,n)

def islands_dfs(mat):
    m,n = len(mat) , len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    directions = [ (-1,-1) , (-1,0) , (-1,1),
                    (0,-1) ,         (0,1),
                    (1,-1) , (1,0)  , (1,1) ]  ## all 8 direction where travel possible
    
    count = 0        
    for i in range(m):
        for j in range(n):
            
            if not visited[i][j] and mat[i][j] == 1:
                dfs(visited,mat,directions,i,j,m,n)
                count += 1
    
    return count

def bfs(visited,mat,directions,row,col,m,n):
    q = deque()
    visited[row][col] = True
    q.append((row,col))
    
    while q:
        row,col = q.popleft()
        for (dr,dc) in directions:
            r,c = row + dr , col + dc
            if 0<=r<m and 0<=c<n:
                if not visited[r][c] and mat[r][c]:
                    q.append((r,c))
                    visited[r][c] = True
                
                
                
                
def islands_bfs(mat):
    m,n = len(mat) , len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    directions = [ (-1,-1) , (-1,0) , (-1,1),
                    (0,-1) ,        , (0,1),
                    (1,-1) , (1,0)  , (1,1) ]  ## all 8 direction where travel possible
    
    count = 0        
    for i in range(m):
        for j in range(n):
            
            if not visited[i][j] and mat[i][j] == 1:
                bfs(visited,mat,directions,i,j,m,n)
                count += 1
    
    return count

    