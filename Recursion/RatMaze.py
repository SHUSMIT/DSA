def ratMaze(i,j,mat,vis,direction,n,ans):
    if i == n-1 and j == n-1:
        ans.append(direction)
        return
    
    #downward  --> row value increases upto n
    if(i+1 < n and not vis[i+1][j] and mat[i+1][j]):  ##prev not visited and also its 1
        vis[i][j] = 1 ## mark visited
        ratMaze(i+1,j,mat,vis,direction+'D',n,ans)
        vis[i][j] = 0 ## backtrack
    
    #left --> col value decreases upto 0  
    if(j-1 >= 0 and not vis[i][j-1] and mat[i][j-1]):
        vis[i][j-1] = 1
        ratMaze(i,j-1,mat,vis,direction+'L',n,ans)
        vis[i][j-1] = 0
    
    #right --> col value increases upto n
    if(j+1 < n and not vis[i][j+1] and mat[i][j+1]):
        vis[i][j+1] = 1
        ratMaze(i,j+1,mat,vis,direction+'R',n,ans)
        vis[i][j+1] = 0
    
    #upward --> row value decreases upto 0
    if(i-1 >= 0 and not vis[i-1][j] and mat[i-1][j]):
        vis[i-1][j] = 1
        ratMaze(i-1,j,mat,vis,direction+'U',n,ans)
        vis[i][j] = 0

## n and mat given
visited = [[0 for _ in range(n)] for _ in range(n)]
direction = ''
ans = list()
ratMaze(0,0,mat,visited,direction,n,ans)
    
    