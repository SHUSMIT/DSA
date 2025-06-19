from collections import deque

def shortest_UDG_topo(edges, V, src):
    # Step 1: Build the adjacency list
    adjL = {i: [] for i in range(V)}
    for u, v in edges:
        adjL[u].append(v)
        adjL[v].append(u)

    # Step 2: Initialize distance array
    dist = [float('inf')] * V
    dist[src] = 0

    # Step 3: BFS traversal
    q = deque([src])
    while q:
        node = q.popleft()
        for neighbour in adjL[node]:
            if dist[node] + 1 < dist[neighbour]:
                dist[neighbour] = dist[node] + 1
                q.append(neighbour)

    return ans
