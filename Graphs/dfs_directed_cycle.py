'''
path visited keeps a record of whether all the dfs call made are in same path, 
once all dfs calls done, backtrack start
we make it 0. if its visited and also path visited, 
theat mean cycle, we return True
'''


def dfs(adjL,node,visited,path_visited):
    visited[node] = 1  ## mark both visited and path_visited
    path_visited[node] = 1
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            if dfs(adjL,neighbour,visited,path_visited):
                return True
            elif path_visited[neighbour]: ## visited as well as path_visited
                return True
                
    path_visited[node] = 0  ## backtrack, and make path = 0
    return False
    

def dfs_cycle(adjL):
    visited = [0 for _ in range(V)]
    path_visited = [0 for _ in range(V)]
    
    for i in range(V):
        if not visited[i]:
            if dfs(adjL,i,visited,path_visited):
                return True
    return False