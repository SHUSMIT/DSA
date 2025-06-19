from collections import deque

def reverse_adj(adjL,V):
    revadj = {i : [] for i in range(V)}
    
    for u in range(V):  ## go for all u
        for v in adjL[u]: ## find corresponding neighbour v
            revadj[v].append(u) ## create a new one where it is reversed
            
    return revadj

    
def safeNodes(adjL,V):
    rev_adjL = reverse_adj(adjL,V)
    ## now reverse, outgoing becomes ingoing
    ## simple bfs topo kahn, if cycle, its anyways not included
    
    indegree = [0 for _ in range(V)]
    
    for i in range(V):
        for neighbour in rev_adjL[i]:
            indegree[neighbour] +=1 
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
            
    safe = list()
    
    while q:
        node = q.popleft()
        for neighbour in rev_adjL[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.append(neighbour)
        safe.append(node)
    
    return sorted(safe)
    
    
    
    
    
    
    