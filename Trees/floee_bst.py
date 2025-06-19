class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def floor_bst(node,x):
    ## floor is the greatest value smaller than equal to x
    answer = -1
    while node:
        if node.val == x:
            return node.val
        elif node.val < x:
            answer = node.val
            node = node.right
        else:
            node = node.left
    return answer
        
    
        
    
    