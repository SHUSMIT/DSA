import heapq

def prim_algo(adjL,V):
    vis = [False] * V
    mst_sum = 0
    mst = []
    pq = []
    heapq.heappush(pq, (0,0,-1))  ## (wt,node,parent) , parent for mst creation

    while pq:
        wt,node,parent = heapq.heappop()
        if vis[node]:
            continue ## skip 
        
        vis[node] = True  # else mark visited
        mst_sum += wt ## add it to sum
        mst.append((node,parent,wt)) # store the tuple of node (u,v,wt)

        for (neighbour,wt) in adjL[node]:
            if not vis[neighbour]: ## not yet part of mst
                heapq.heappush(pq,(wt,neighbour,node)) ## push it into pq
    
    return mst_sum,mst

