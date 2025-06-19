from collections import deque

def topo_kahn(adjL,V):
    indegree = [0 for _ in range(V)]
    ##create in degree
    for i in range(V):
        for neighbour in adjL[i]:
            indegree[neighbour] += 1
    
    q = deque()
    ## push all 0 indegree
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
            
    topo = list()
    while q:
        node = q.popleft() ##pop it
        for neighbour in adjL[node]: 
            indegree[neighbour] -= 1  ##reduce indegree of neighbour by 1
            if indegree[neighbour] == 0: # if its 0, push it 
                q.append(neighbour)
        topo.append(node)
    
    return topo