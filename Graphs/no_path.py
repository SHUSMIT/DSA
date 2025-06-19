import heapq

def ways_to_arrive(adjL,V):
    ## same dikstra, but when the equlity of distances hold, just increase the count ways by 1
    ## total ways to reach = total way 1 + total way 2 + total way 3... this goes on
    mod = int(1e9+7)

    distance = [float('inf')] * V
    ways = [0 for _ in range(V)]
    distance[0] = 0 ## assume 0 is starting and v-1 is the ending
    ways[0] = 1
    pq = []

    heapq.heappush(pq,(0,0)) ## (distance,node)
    while pq:
        d_node,node = heapq.heappop(pq)
        for (neighbour,dist) in adjL[node]:
            if d_node + dist < distance[neighbour]:
                distance[neighbour] = d_node + dist
                heapq.heappush(pq,(distance[neighbour],neighbour))
                ways[neighbour] = ways[node] ## this is the first time it has been visited, so update with ways by which node was visited

            elif d_node + dist == distance[neighbour]:
                ways[neighbour] = ( ways[neighbour] + ways[node] ) % mod  ## again visited, so now add it to the current one
    
    return ways[V-1] % mod
