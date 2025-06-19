def dfs(node,vis,st,adjL):
    vis[node] = 1
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            dfs(neighbour,visited,st,adjL)
    st.append(node) ## when no more calls, backtrack, push into stack

def topo_dfs(adjL,V):
    visited = [False] * V
    st = list()
    
    for i in range(V):
        if not visited[i]:
            dfs(i,visited,st,adjL)
    
    return st[::-1]  ## reverse and return 