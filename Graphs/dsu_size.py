class DisjointSetUnion:
    def __init__(self,n):
        self.size = [1 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]
    
    def find_Uparent(self,node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find_Uparent(node) ## we recursively find, equal to for assignment so that next time fast

        return self.parent[node]
    
    def union_size(self,x,y):
        up_x = self.find_Uparent(x)
        up_y = self.find_Uparent(y) ## finding ultimate parent of x,y

        if up_x == up_y:
            return ## both same
        
        elif self.size[up_x] > self.size[up_y]: ## size of x is greater than y (ultimate)
            self.parent[up_y] = up_x # smaller gets to larger
            self.size[up_x] += self.size[up_y] ## add that size
        
        else:
            self.parent[up_x] = up_y
            self.size[up_y] += self.size[up_x] ## equality case also