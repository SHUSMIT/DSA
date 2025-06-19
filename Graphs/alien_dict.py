def dfs_topo(node,adjL,stack,visited):
    visited[node] = True
    
    for neighbour in adjL[node]:
        if not visited[neighbour]:
            dfs_topo(neighbour,adjL,stack,visited)
    
    stack.append(node) ## backtrack

def alien_dictionary(arr,k):
    ## k first alphabets 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    dictionary = { alphabet[i] : i for i in range(k) } ## maps alphabet to numbers
    rev_dictionary = { i : alphabet[i] for i in range(k)} ## for returning back
    
    adjL = [[] for _ in range(k)]
    
    for i in range(len(arr)-1):

        for j in range(min(len( arr[i], arr[i+1] ))):
            if arr[i][j] != arr[i+1][j]:
                adjL[ dictionary[ arr[i][j]] ].append( dictionary[ arr[i+1][j] ] )  ## create the adjacency list
                break 
        
        else len(arr[i]) > len(arr[i+1]):
            ## violation, above worked but no break as all equal but case like abcd is before abc
            return ''
    
    visited = [False] * k
    stack = list()
    for i in range(k):    
        if not visited[i]:
            dfs_topo(i,adjL,stack,visited)
            
    if len(stack) != k: ## cyclic dependecny
        return ''
        
    alien = ''.join(rev_dictionary[i] for i in reversed(stack))
    return alien
    