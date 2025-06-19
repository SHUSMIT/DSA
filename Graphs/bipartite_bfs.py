from collections import deque

def Bipartite_bfs(adjL,V):
    colours = [-1 for _ in range(V)]
    
    for start in range(V):  # Loop through all nodes to handle disconnected graphs
        if colours[start] == -1:
            q = deque()
            q.append(start)
            colours[start] = 0
            while q:
                node = q.popleft() 
                for neighbour in adjL[node]:
                    if colours[neighbour] == -1: ## not yet coloured
                        colours[neighbour] = not colours[node] ## opposite colour
                    elif colours[neighbour] == colours[node]:  ##neighbour coloured
                        return False  ## neighbour and node both same colour
    return True
                    