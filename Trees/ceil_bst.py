class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def ceil_bst(node,x):
    ## ceil of x is the lowest value >= x
    answer = -1
    while node:
        if node.val == x:
            return node.val
        elif node.val >= x:
            answer = node.val
            node = node.left # got something bigger now move left
        else:
            node = node.right
            
    return answer
    
        
    
    