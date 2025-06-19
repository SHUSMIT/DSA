def dfs(adjL,colours,node,node_colour):
    colours[node] = node_colour  ## change colour from adjacent node
    for neighbour in adjL[node]:
        if colours[neighbour] == -1:
            if not dfs(adjL,colours,neighbour, 1 - node_colour): ## false return, return false , pass the opp of node_colour
                return False
        elif colours[neighbour] == node_colour:  ##not bipartitie, so recursuvely return False
            return False
    return True



def Bipartite_dfs(adjL,V):
    colours = [-1 for _ in range(V)]
    
    for node in range(V):  # Loop through all nodes to handle disconnected graphs
        if colours[node] == -1:
            colours[node] = 0  ##initial for each component
            if not dfs(adjL,colours,node,colours[node]): ## call
                return False ## if false returned, then return false
    return True

                    