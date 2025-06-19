from collections import deque

def cycle_bfs(V,adjL):
    
    visited = [False] * V
    
    for i in range(V):
        if not visited[i]:
            
            q = deque()
            # (node,parent)
            q.append((i,-1))
            visited[i] = True
            
            while q:
                node,parent = q.popleft() ## keep paret node track
                for neighbour in adjL[node]: # iterate all neighbour in node
                    if not visited[neighbour]: ## if not visited mar
                        visited[neighbour] = 1
                        q.append((neighbour,node))
                    elif neighbour != parent: ## if visited that means it has come from parent,ie, the double connection (1->3 and 3->1)
                    # while 1->3 it must have been marked, so 3 would see 1 
                        return True ## but if any other node marked, means cycle 
                        
                        ### 5 
                        ###     9
                        ### 7
                        ### 9 - {5,7}..... 87 already marked, 9 already marked via 7..  say now at 9, iterate
                        ### (node,parent) = (9,5) ... iterate through 9, 5 visited = parent but 7 is not, but its visited, means cycle
    return False