class disjoint_set_union:
    def __init__(self,n): ## n is size
        ## rank and parent array
        self.rank = [0 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]
    
    ## function for find parent
    def find_Uparent(self,node):
        if self.parent[node] == node:
            return node
        
        return self.parent[node] = self.find_Uparent(node) ## else we keep finding, equal sign is given so that path compression happen
    
    def union_by_rank(self,x,y): ## smaller rank one joins the larger
        up_x = self.find_Uparent(x) ## up is ultimate parent
        up_y = self.find_Uparent(y)

        if up_x == up_y: ## same parent, no add
            return
        
        elif self.rank[up_x] < self.rank[up_y]: ## to join, we check rank of ultimate parent
            self.parent[up_x] = up_y

        elif self.rank[up_y] < self.rank[up_x]:
            self.parent[up_y] = up_x

        else: ## both equal, join either
            self.parent[up_y] = up_x
            self.rank[up_x] += 1 ## increase the rank by 1