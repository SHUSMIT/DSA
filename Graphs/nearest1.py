from collections import deque

def nearest1(mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    visited = [[0 for _ in range(n)] for _ in range(m)]
    dist = [[0 for _ in range(n)] for _ in range(m)]  ## keep a distance matrix with all 0

    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    ## row,col,distance
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                q.append((i, j, 0))
                visited[i][j] = 1
                dist[i][j] = 0
    
    while q:
        row,col,distance = q.popleft()
        for dr, dc in direction:
            r, c = row + dr, col + dc 
            if 0 <= r < m and 0 <= c < n:
                if not visited[r][c]:
                    visited[r][c] = 1
                    q.append((r,c,distance+1))
                    dist[r][c] = distance + 1
    return dist











