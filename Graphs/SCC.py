def dfs_traversal(node,adjL,visited,dfs):
    visited[node] = True
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            dfs_traversal(neighbour,adjL,visited,dfs)
    dfs.append(node) ## backtrack


def strongly_connected(adjL,V):
    dfs = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs_traversal(i,adjL,visited,dfs)

    dfs.reverse() ## reverse the dfs array to sort as per time, last one was first visited ( depth )
    visited = [False] * V ## re make the visited array

    rev_adjL = {i : [] for i in range(V)}

    for u in adjL:
        for v in adjL[u]:
            rev_adjL[v].append(u) ## reverse the node
    
    scc_number = 0
    scc=[]
    for node in dfs: ## in oreversed order of dfs now visit
        if not visited[node]:
            dfs_curr = []
            dfs_traversal(i,rev_adjL,visited,dfs_curr)
            scc_number +=1
            scc.append(tuple(dfs_curr)) ## add it to scc list
    
    return scc_number,scc


        
    
