class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def morrisTraversal(node):
    inorder = []
    current = node
    while current:
        
        if not current.left:  ##left not exist
            inorder.append(current.val) ##its node so add it 
            current = current.right  ## move right 
            
        else: ##current left exist
        
            prev = current.left  ## keep a record of prev/node 
            
            while prev.right and prev.right != current: ## this means that there is no thread. go right extreme
                prev = prev.right ##go right 
            
            if prev.right == None: # reached the end right, so now point to root/current
                prev.right = current
                current = current.left ## move left now
            
            else: ## already connected to current 
                prev.right = None ## break the link
                inorder.append(current.val) ## add the current
                current = current.right
            
    return inorder 
                
                
                
            
            
                