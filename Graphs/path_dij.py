import heapq

# adjL is a list of adjacency lists: adjL[u] = [(v1, wt1), (v2, wt2), ...]

def dijkstra_algo(adjL,V,src,dest):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0,src))
    parent = [i for i in range(V)] ## makes a parent ( 0 based index )
    ## take the pq
    while pq:
        d_node,node = heapq.heappop(pq)  ## pop it
        for (neighbour,weight) in adjL[node]:
            if d_node + weight < dist[neighbour]:  ## if dist to reach node+weight < previous dist to reach neighbout
                dist[neighbour] = d_node + weight ## update it
                parent[neighbour] = node   ## make a record of parent/node 
                heapq.heappush(pq,(d_node+weight, neighbour)) ## push it into a min heap

    ans = []
    current = dest
    while parent[current] != current:
        ans.append(current)
        current = parent[current]
    
    ans.append(src)
    return reversed(ans)

