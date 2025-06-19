class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def childSum(node):
    if node is None:
        return None
    
    childSum = 0  ##keep an initial sum
    if node.left:
        childSum += node.left.val  ## add left
    if node.right:
        childSum += node.right.val  ## add right
    
    if childSum >= node.val:
        node.val = childSum  ## if root is smaller, update it 
    if childSum < node.val:
        if node.left: ##if left/right is smaller, update it with roots value
            node.left.val = node.val
        if node.right:
            node.right.val = node.val
    
    childSum(node.left) ##recursively do it for all
    childSum(node.right)
    back_track_sum = 0  ##backtrack now wth initial = 0
    
    if node.left:
        back_track_sum += node.left.val ## same above where left and right add
    
    if node.right:
        back_track_sum += node.right.val
    
    if node.left or node.right: ## if not leaf add it 
        node.val = back_track_sum
    
    
    
    
    
    