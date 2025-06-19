from collections import deque

def rotten_oranges(mat):
    m,n = len(mat),len(mat[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    modified_mat = [row[:] for row in mat]
    
    direction = [(0,-1), (-1,0), (1,0), (0,1)]
    
    q = deque()
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 2:
                q.append((i,j))  ## add all 2/rotten into q
                visited[i][j] = 1
    
    time = 0
    
    while q:
        cur_len = len(q) ## for iterating all 2's in current
        flag  = False
        
        for i in range(cur_len): ## till all current 2's visited
            row,col = q.popleft()
            for (dx,dy) in direction:
                r = row + dx ## all direction
                c = col + dy
                if 0<=r<m and 0<=c<n:
                    if not visited[r][c] and mat[r][c] == 1: ## not visited and its fresh
                        modified_mat[r][c] = 2 # rotten it
                        visited[r][c] = 1
                        flag = True # signifies rottening
        if flag: # if atleast 1 rotten, then only time increase
            time += 1
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and modified_mat[i][j] == 1:
                ##could not rotten
                return -1

    return time
            
                        
        
        
    