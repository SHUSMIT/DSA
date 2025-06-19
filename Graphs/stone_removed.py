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

## array of coordi of stones
def stones_removal(arr):
    max_row_val = max(row for (row,col) in arr)
    max_col_val = max(col for (row,col) in arr)

    ds = DisjointSetUnion(max_row_val+max_col_val)

    row_map = {}
    col_map = {} 

    ## basically we are assigning all rows a node value and all col a node value that has stone ( arr )
    ## row0 =1 ,row1 = 2 etc, to prevent same node, col is offset

    nodes = set() # keeps a record of all nodes
    ## we store the node value of row,col index

    for (row,col) in arr: ## offset for column because it has to be unique node for dsu
        ds.union_size(row,col+max_row_val+1)
        nodes.add(row)
        nodes.add(col+max_row_val+1) ## keeps only unique
    
    parent = set()
    for node in nodes:
        parent.add(ds.findUparent(node))
    
    return len(arr) - len(parent)

 
    

        
    
