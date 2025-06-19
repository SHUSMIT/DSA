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


def connected_components(edges,V):

    ds = DisjointSetUnion(V)

    extras = 0 
    for (u,v) in edges:
        if ds.findUparent(u) == ds.findUparent(v):  ## both have same parent
            extras += 1  ## if they didnt have a common parent (< or > ) then we used to apply kruskal algo to connect the edges with wt to form mst. 
            ## this would been continue/ignored ( after sorting wts ofc )
        else:
            ds.union(u,v) ## else we form edges

    countCN = 0

    for i in range(V):
        if ds.findUparent(i) == i:
            countCN += 1 ## if parent is itseld, its ultimate so ultimate ++
    
    if countCN - 1 == extras:
        return extras
    
    return -1

