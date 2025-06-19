import heapq

def dijkstra(adjL, src, V):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d_node, node = heapq.heappop(pq)
        
        for neighbour, wt in adjL[node]:
            if d_node + wt < dist[neighbour]:
                dist[neighbour] = d_node + wt
                heapq.heappush(pq, (dist[neighbour], neighbour))

    return dist

def city_least_neighbours(adjL, V, k):
    min_neighbours = float('inf')
    result_city = -1

    for city in range(V):
        distances = dijkstra(adjL, city, V)
        count = sum(1 for d in distances if 0 < d <= k)  # count neighbors within threshold, excluding self

        # if fewer neighbors, or same number but larger city index
        if count <= min_neighbours:
            min_neighbours = count
            result_city = city

    return result_city
