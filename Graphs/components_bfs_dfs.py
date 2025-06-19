from collections import deque

def adj_Mat_to_L(matrix):
    n = len(matrix)
    adjL = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and i != j:  # Exclude self-loops if not needed
                adjL[i].append(j)
    return adjL

def bfs(node,visited,adjL):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        node = q.popleft()
        for neighbours in adjL[node]:
            if not visited[neighbours]:
                q.append(neighbours)
                visited[neighbours] = True
    
def dfs(node,visited,adjL):
    visited[node] = True ## mark the node
    for neighbours in adjL[node]:  ## if not visited, iterate, keep going deep
        if not visited[neighbours]:
            dfs(neighbours,visited,adjL)

def provinces_bfs_method(adjL,V):
    visited = [False] * V
    count = 0
    
    for i in range(V):
        if not visited[i]:
            bfs(i,visited,adjL)
            count += 1
    
    return count
    
def provinces_dfs_method():
    visited = [False] * V
    count = 0
    
    for i in range(V):
        if not visited[i]:
            dfs(i,visited,adjL)
            count += 1
    
    return count
    
