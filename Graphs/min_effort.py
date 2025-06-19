import heapq


def min_effort(mat,src_row,src_col,end_row,end_col):
    m,n = len(mat),len(mat[0])
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    ## dist mat is the effort one
    pq = []
    heapq.heappush(pq,(0,src_row,src_col))
    dist[src_row][src_col] = 0

    directions = [(-1,0),(1,0),(0,1),(0,-1)]

    while pq:
        effort,row,col = heapq.heappop(pq) ## DIFF,ROW,COL

        if (row, col) == (end_row, end_col):
            return dist[end_row][end_col]

        for (dr,dc) in directions:
            r = row+dr
            c = col+dc
            if (0<=r<m) and (0<=c<n):

                curr_effort = abs(mat[row][col] - mat[r][c]) ## fin the curent effort
                new_effort = max(effort, curr_effort)  ## we want max of all efforts in the path that has to be minimised
                
                if new_effort < dist[r][c]: ## if the max of all is less, we update
                    dist[r][c] = new_effort
                    heapq.heappush(pq, (new_effort, r, c))


    return -1     