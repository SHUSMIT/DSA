class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def LCA(node,x,y):
    
     if node is None:
        return None
        
    if node.val == x or node.val ==y:
        return node.  ## cant say whether its on left or right
    
    if x<node.val<y or y<node.val<x:
        return node.val
    
    if node.val > x and node.val >y:
        LCA(node.left,x,y)
    else:
        LCA(node.right,x,y)
    
    