class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node): ## left -> root -> right
    if node == None: #leaf reached
        return

    inorder(node.left) ##move left
    print(node.data)  ## print the root
    inorder(node.right) ## move right

def preorder(node): ## root -> left -> right
    if node ==None:
        return 
    
    print(node.data)  #print the root
    preorder(node.left)
    preorder(node.right)


def postorder(node): # left,right,root
    if node == None:
        return 
    
    postorder(node.left)
    postorder(node.right)
    print(node.data)
    