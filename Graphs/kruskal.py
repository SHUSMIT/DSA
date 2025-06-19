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


## logic us
def kruskal(adjL,V):
    ## (wt,u,v) we have to make from given u : {wt,v}
    edges_tuple = []
    for i in range(V):
        for (wt,neighbour) in adjL[i]:
            edges_tuple.append((wt,i,neighbour))
    
    edges_tuple.sort(key = lambda x: x[0]) ## means sort based on first index

    mst_wt = 0
    mst = []

    ds = DisjointSetUnion(V) ## create a ds of DSU

    for (wt,u,v) in edges_tuple:
        ## if belong to same ds we include it
        ## else we ignore it
        if ds.findUparent(u) != ds.findUparent(v):
            mst_wt += wt
            mst.append((u,v,wt))
            ds.union(u,v)
    
    return mst_wt,mst

    
    
