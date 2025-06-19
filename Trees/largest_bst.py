class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Value:
    def __init__(self, bigger = float('-inf'), smaller = float('inf'),size = 0):
        self.max_value = bigger
        self.min_value = smaller 
        self.max_current_size = size

def largest_bst(node):
    if node is None:
        return Value()  ## if nothing a dummy value to be return
    
    left = largest_bst(node.left) ## move left and go the end
    right = largest_bst(node.right)   ## postorder -> left,right,node
    
    ##once all left and right taversal of current root has been done
    
    if left.max_value < node.val < right.min_value: ## valid bst
        
        max_current_size = 1 + left.max_current_size + right.max_current_size ## 1 + x + y for current node
        max_value = max(node.val, left.max_value)  ## update new max, its always max of left, incase its None, updated
        min_value = min(node.val, right.min_value) ## same above
        return Value(max_value,min_value,max_current_size) ## return the value of root , which is later to be used
        
    else:
        # violated, so impossible case of max = inf, min = -inf and size = last max size
        max_current_size = max(left.max_current_size,right.max_current_size)
        return(float('inf'),float('-inf'),max_current_size)
        
        
        
        
        
        
        