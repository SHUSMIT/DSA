def floyd_warshall(mat,V):
    dist = [row[:] for row in mat]
    for i in range(V):
        for j in range(v):
            for k in range(V):
                if dist[i][k] != float('inf') and dist[k][i] != float('inf'):
                    dist[i][j] = min(dist[i][j] , dist[i][k]+dist[k][j])
    return dist
    
    ## negative cycle
    for i in range(V):
        dist[i][i] < 0:
            return -1 ## neagative cycle meas diagonal is less than 0