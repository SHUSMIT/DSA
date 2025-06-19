class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def isBST(node,up_bound=float('inf'),low_bound=float('-inf')):
    if node is None:
        return True
    
    if not (low_bound < node.val < up_bound):
        return False
    
    left = isBST(node.left,node.val,low_bound)
    right = isBST(node.right,up_bound,node.val)
    return left and right
    
    