from collections import deque

def dfs_traversal(adjL,start,dfs,visited):
    
    visited[start] = True ## mark the node as visited and append it
    dfs.append(start)
    
    for neighbour in adjL[start]: ## go over neighbour, if not visited, keep calling recursively
        if not visited[neighbour]:
            dfs_traversal(adjL,neighbour,dfs,visited) 
            
## assume adj: is given
def dfs_full(adjL,start,vertices):
    dfs = []
    visited = [False] * len(vertices)
    dfs.append(start)
    dfs_traversal(adjL,start,dfs,visited) ##  for first call with start
    
    ## for disconnected
    for i in range(vertices):
        if not visited[i]:
            dfs_traversal(adjL,i,dfs,visited)
    
    
    
    