class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def delete(root,target):
    if not root:
        return None
    
    if root.val == target:
        return childjoiner(root)
    
    dummy_store = root
    
    while root:
        
        if root.val > target: # go left
        ## we now go left and right to find the parent of target 
            if root.left and root.left.val == target: ## left of root has it
                root.left = childjoiner(root.left, target) ## we would update it
                break
            else:
                root = root.left ## keep searching
        
        else:
            if root.right and root.right.val == target:
                root.right = childjoiner(root.right,target)
                break
            else:
                root = root.right
    
    return dummy_store


def childjoiner(node,target):
    if not node.right: ## no right so 
        return node.left ## directly directly attach left of passed node ( its actaully root.left.left)
    if not node.left:
        return node.right
    
    else:
        node_left_tree = node.left ## store the node_left_tree
        right_extreme_left = find(node.left)  ## find the right extreme
        right_extreme_left.right = node.right  ## join the right extreme of left subtree to right subtree start
        
        return node_left_tree ## return the node_left_tree

def find(node):
    while node.right:
        node = node.right ## keep moving
    return node
        
        
    
         
    
    
    