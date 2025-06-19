from collections import deque

def cheapest_ksteps(adjL,V, src, end, k):
    dist = [float('inf')] * V
    dist[src] = 0
    # no need of pq, it works still, as steps increase by 1
    # we store a q (steps,dist,node)
    q = deque()
    q.append((0,0,src))

    while q:
        steps,d_node,node = q.popleft()

        if k+1 == steps: ## number of steps readched
            continue ## so we skip searching for that node's neighbour and go to next node in q

        for (neighbour,weight) in adjL[node]:
            if d_node + weight < dist[neighbour] and steps <= k: 
                dist[neighbour] = d_node + weight ## simple disjktra
                q.append((steps+1,dist[neighbour], neighbour))

    if dist[end] == float('inf'):
        return -1

    return dist[end]
