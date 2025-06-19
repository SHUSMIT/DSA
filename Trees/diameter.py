class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def diameter(node,dia):
    if node == None:
        return 0
        
    lh = diameter(node.left, dia)
    rh = diameter(node.right, dia)
    dia = max(dia,lh+rh) ## for each node, ocnsider it picvot and find left and right node sum
    
    return 1 + max(lh,rh) 