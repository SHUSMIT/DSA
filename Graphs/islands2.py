class DisjointSetUnion:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    def findUparent(self,node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.findUparent(self.parent[node])
        
        return self.parent[node]
    
    def union(self,x,y):
        up_x = self.findUparent(x)
        up_y = self.findUparent(y)

        if up_x == up_y:
            return
        
        elif self.size[up_x] > self.size[up_y]:
            self.parent[up_y] = up_x
            self.size[up_x] += self.size[up_y]
        else:
            self.parent[up_x] = up_y
            self.size[up_y] += self.size[up_x]


def islands2(mat,operations):
    m,n = len(mat),len(mat[0])
    directions = [(-1,0) , (0,1) , (1,0) , (0,-1) ]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    ds = DisjointSetUnion(m*n) # total matrix size
    ## if mat is 1 and and not visited, we increase counter.
    ## then explore neighbour, if 1's there, we do union and reduce counter for every neighbour 1

    counter = 0
    ans_count = []
    ## operatins has (row,col) that has to be marked 1/islands
    ## node number ( 0 based ) -> row * n + col , n is total col number

    for (row,col) in operations:
        if visited[row][col] == 1:
            ans.append(count) ## its alsready visited,operation done (1,1) again (1,1)
            continue
        
        node = row * n + col
        visited[row][col] = 1 # mark visited
        count += 1 ## assume its a seperate island

        for (dr,dc) in directions:
            r,c = row+dr,col+dc
            if 0<=r<m and 0<=c<n: ## valiity check 

                adjNode = r * n + c
                if visited[r][c]:  # meaning an island, prev considered single but now reachable
                    if ds.findUparent(node) != ds.findUparent(adjNode): ## diff up means diff island considered -> connect them, reduce counter
                        count -= 1
                        ds.union(node,adjNode) ## do an union

        ans.append(count) ## store the count after for loop
    
    return ans