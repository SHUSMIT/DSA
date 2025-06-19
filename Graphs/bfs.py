from collections import deque

def adjencyList(vertices, edges):
    adjL = {v: [] for v in vertices}
    for (u, v) in edges:
        adjL[u].append(v)
        adjL[v].append(u)
    return adjL

def bfs_traverse(edges, vertices, start):
    adjL = adjencyList(vertices, edges)
    visited = [False] * len(vertices) ## create a visited array
    q = deque() #queue
    bfs = [] # bfs array
    q.append(start) ## add it 
    visited[start] = True # mark true

    while q:
        node = q.popleft() # pop it
        for neighbour in adjL[node]: # iterate through all neighbour
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True
        bfs.append(node)

    # Handle disconnected components
    for i in range(len(vertices)):
        if not visited[i]:
            q.append(i)
            visited[i] = True
            while q:
                node = q.popleft()
                for neighbour in adjL[node]:
                    if not visited[neighbour]:
                        q.append(neighbour)
                        visited[neighbour] = True
                bfs.append(node)
                
    return bfs

