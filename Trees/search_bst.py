class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def search_bst(node,target):
    ## L < root < R
    while node:
        if target == node.val:
            return True
        
        if target > node.val:
            node = node.right
        else:
            node = node.left
    
    return False
        
    
    