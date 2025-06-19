class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def inorder_succesor(node,val):
    ##succesor is value immediately greater than it
    
    succesor = None
    
    while node:
        if node.val <= val: ## value is less, so definietly left cant be
            node = node.right
            
        if node.val > val:
            succesor = node.val ## first greater, might be lets see
            node = node.left ## to check if smaller exist
            
        # else: ##equal
        #     ##left most of right subtree of node. right doesnt exist we return succesor
            
        #     if node.right:
        #         curr = node.right
                
        #         while curr.left:
        #             curr = curr.left  ## left most of right subtree
                    
        #         return curr.val
        #     break
        
    return succesor if succesor else None
    
    
    