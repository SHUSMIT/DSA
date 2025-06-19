from collections import deque

def create_adjL(adjL,arr):
    for (u,v) in arr:
        adjL[u].append(v)

def preRequisite(arr,V):
    ## crate adjL
    adjL = {x : [] for x in range(V)}
    create_adjL(adjL,arr)
    
    ## now topologically sort, if possible then return else -1 
    # indegree create
    indegree = [0 for _ in range(V)]
    for i in range(V):
        for neighbour in adjL[i]:
            indegree[neighbour] += 1
    
    # create q and push all in 0 into it
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
            
    topo = list()
    
    while q:
        node = q.popleft()
        for neighbour in adjL[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                q.append(neighbour)
                
        topo.append(node)
        
    if len(topo) == V:
        return topo
    else:
        return -1
    