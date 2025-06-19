class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def height(root):
    if node == None:
        return 0 ##leaf
    
    lh = height(node.left)  ##go left
    rh = height(node.right) ##go right
    
    return 1 + max(lh,rh)

def isBST(root):
    if node == None:
        return 0
    
    lh = isBST(node.left)
    rh = isBST(node.right)
    ##make two changes, if left height and right height akready calulated use them
    if lh == -1 or rh == -1:
        return -1
    
    if abs(lh-rh) > 1:
        return -1
    
    return 1 + max(lh,rh) 