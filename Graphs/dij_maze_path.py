import heapq


def dij_maze(mat,src_row,src_col,end_row,end_col):
    m,n = len(mat),len(mat[0])
    dist_mat = [[float('inf') for _ in range(n)] for _ in range(m)]
    directions = [(-1,0), (0,1) , (1,0) , (0,-1)]

    parent = [[(row,col) for col in range(m)] for row in range(n)]

    ## (dist,(row,col))
    pq = []
    heapq.heappush(pq,(0,src_row,src_col))
    dist_mat[src_row][src_col] = 0

    while pq:
        dist_node,row,col = heapq.heappop(pq)
        if (row,col) == (end_row,end_col): ## found

            path = []
            curr = (end_row, end_col)
            while curr != (src_row, src_col):
                path.append(curr)
                curr = parent[curr[0]][curr[1]] ## row col of parent-> 2d matrix storing row,col
            path.append((src_row, src_col))
            path.reverse()

            return dist_mat[end_row][end_col], path  ## its a greedy algo, so if I get it, it would be shortest so returned 


        for (dr,dc) in directions:
            r,c = dr+row,dc+col 
            if (0<=r<m) and (0<=c<n): ## go in all directiona
                if dist_node + 1 < dist_mat[r][c] and mat[r][c] == 1: ## if small ,update/dijskitra and also the cell is 1
                    dist_mat[r][c] = dist_node + 1 ## every left,top,righ,down movement is unit, step
                    heapq.heappush(pq,(dist_node+1,r,c)) ## push it
                    parent[r][c] = (row,col)
    
    return -1,-1
    

