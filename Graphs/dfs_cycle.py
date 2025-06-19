
def dfs(adjL,visited,node,parent):
    visited[node] = True 
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            visited[neighbour] = True
            if dfs(adjL,visited,neighbour,node): ## (node,parent) , so here neighbour is node and parent is node
                return True  ## if the recursion call return true, return true continuosly 
                
        elif parent != neighbour:  ## parent not equals the neighbour of node but its visited
            return True
    
    return False
 
def cycle_dfs(adjL,V):
    visited = [False] * V
    
    for i in range(V):
        if not visited[i]:
            if dfs(adjL,visited,i,-1) == True:
                return True
                break
    
    return False
            
    