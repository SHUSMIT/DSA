import heapq

# adjL is a list of adjacency lists: adjL[u] = [(v1, wt1), (v2, wt2), ...]

def dijkstra_algo(adjL,V,src):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0,src))

    ## take the pq
    while pq:
        d_node,node = heapq.heappop(pq)  ## pop it
        for (neighbour,weight) in adjL[node]:
            if d_node + weight < dist[neighbour]:  ## if dist to reach node+weight < previous dist to reach neighbout
                dist[neighbour] = d_node + weight ## update it
                heapq.heappush(pq,(d_node+weight, neighbour)) ## push it into a min heap

    return dist
