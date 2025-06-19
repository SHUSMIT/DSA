class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def insert(root,value):
    if root is None:
        return Node(value)
    
    current = root
    while current:
        if value > current.val: ## if value greater go right
            if current.right: 
                current = current.right 
            else:
                node = Node(value) ## if nothing of right there
                current.right = node ## point right to node if right not present
                break
        else:
            if current.left:
                current = current.left
            else:
                node = Node(value)
                current.left = node
                break
    return root

