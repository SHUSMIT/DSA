def bell_man(adjL,V):
##v-1 time son all edges
    dist = [float('inf')] * V
    dist[src] = 0
    for i in range(V): ## v-1 iteration
        for (u,v,wt) in adjL:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]: ## relaxation
                dist[v] = dist[u] + wt 
## negative cycle,nth
    for (u,v,w) in adjL:
        if dist[u] != float('inf') and dist[u] + wt < dist[v]: ## still reduced
            return -1
    
    return dist
