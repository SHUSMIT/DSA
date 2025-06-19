class DisjointSetUnion:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    def findUparent(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUparent(self.parent[node]) ## recursively point all to parent for fast lookup
        return self.parent[node]
    
    def union_size(self,x,y):
        up_x,up_y = self.findUparent(x),self.findUparent(y)
        if up_x == up_y: ## same so ignore
            return
        
        elif self.size[up_x] > self.size[up_y]: #disjoin, x > y
            self.parent[up_y] = up_x
            self.size[up_x] += self.size[up_y]
        
        else:
            self.parent[up_x] = up_y
            self.size[up_y] += self.size[up_x]

## we can store all 0's turn into one and check
def large_islands(mat):
    m,n = len(mat),len(mat[0])
    ds = DisjointSetUnion(m*n)
    count_zero = 0
    
    ## we connect all components first
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    for i in range(m):
        for j in range(n):
            
            if mat[i][j] == 0: ## check edge 
                count_zero += 1
            
            if mat[i][j]: ## skip 0 
                node = i * n + j
                for (dr,dc) in directions:
                    r,c = i+dr,j+dc
                    if 0<=r<m and 0<=c<n and mat[r][c]==1: ## neighbours
                        adjNode = r * n + c
                        ds.union_size(node,adjNode)
    
    if count_zero == 0:
        return m*n ## no zero, no flip hence
        
    ##now we go across all 0, if neighbour 1, we put its ultimate parent into set, then calulate the size
    max_size = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0: #check adjacent is1, then convertible

                components = set() ## to ensure sam parent not again calulated

                for (dr,dc) in directions:
                    r,c = i+dr,j+dc
                    if 0<=r<m and 0<=c<n and mat[r][c]==1: 
                        adjNode = r * n + c # we need ultimate parent
                        components.add(ds.findUparent(adjNode)) ## this ensures no repeatation of same component
                
                #after checking all directions
                size = 0
                for i in components:
                    size += ds.size[i] ## get all component sizes
                
                max_size = max(max_size , size + 1) # itself also


    return max_size
