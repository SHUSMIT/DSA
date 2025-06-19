class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

def lefthalf(node,boundary):
    
    current = node.left  ## move now to left
    while current:
        if( not isLeaf(current) ): 
            boundary.append(current.data) ## add if not leaf
        if current.left:  ## move left as possible
            current = current.left
        else:
            current = current.right

def righthalf(node,boundary):
    
    temp = []
    current = node.right
    while current:
        if (not isLeaf(current)):
            temp.append(current.data)
        if current.right:
            current = current.right
        else:
            current = current.left
    
    temp.reverse()
    boundary.extend(temp)
    
    
    
def leave(node,boundary):
    if isLeaf(node):
        boundary.append(node.data)
    
    if node.left:
        leave(node.left,boundary)
    if node.right:
        leave(node.right,boundary)

def isLeaf(node):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        return True
    else:
        return False
    

def boundary_traversal(node,boundary):
    if node is None:
        return boundary
    
    boundary.append(node.data)
    lefthalf(node,boundary)
    leave(node,boundary)
    righthalf(node,boundary)
    