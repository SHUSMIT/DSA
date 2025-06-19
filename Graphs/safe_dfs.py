'''
path visited keeps a record of whether all the dfs call made are in same path, 
once all dfs calls done, backtrack start
we make it 0. if its visited and also path visited, 
theat mean cycle, we return True
'''


def dfs(adjL,node,visited,path_visited,check):
    
    visited[node] = 1  ## mark both visited and path_visited
    path_visited[node] = 1
    check[node] = 0  ## assune the node is unsafe, explore all its path 
    
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            if dfs(adjL,neighbour,visited,path_visited,check):
                ## that's a cycle so the node can never be safe
                return True
        elif path_visited[neighbour]: ## visited as well as path_visited
            ## its cycle so it cannot be, so return True and check - 0
            return True
    
    check[node] = 1 ## it compelted, and hecne reached terminal, so backtrack and keep check of that node = 1           
    path_visited[node] = 0  ## backtrack, and make path = 0
    return False
    

def safe_node_dfs(adjL,V):
    visited = [0 for _ in range(V)]
    path_visited = [0 for _ in range(V)]
    safe_node = list()
    check = [0 for _ in range(V)]
    for i in range(V):
        if not visited[i]:
            dfs(adjL,i,visited,path_visited,check)
            
    for i in range(V):
        if check[i] == 1:
            safe_node.append(i)
    return safe_node