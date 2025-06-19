class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def LCA(node,nodeA,nodeB):
    if node is None: ## if we reach end we return none
        return None

    if node == nodeA or node == nodeB: ## if node is A or B we return that node
        return node
    
    left = LCA(node.left,nodeA,nodeB) ##left call
    right = LCA(node.right,nodeA,nodeB)  ## right call
    
    if left and right: ## we return something only when we get 
    ##if from left and right we get both A and B
        return node  ## we return that node as answer
    
    return left if left else right  ## we return left/right call of that node ( null,node) -> node