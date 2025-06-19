class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(left,right):     ## node left right ||| node right left comparison 
    if left is None and right is None:
        return left == right
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    
    return isSymmetric(left.left , right.right) and isSymmetric(left.right, right.left)

def symmetric(head):
    return (head is None) or (isSymmetric(node.left, node.right))