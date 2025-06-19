class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def get_path(node,arr,target):
    if node is None:
        return False  ##reached the left/right
    
    arr.append(node) ##add it to array
    if node.val == target: ##if it equals target we return True
        return True
    
    if get_path(node.left,arr,target) or get_path(node.right,arr,target): ##recursively check both left and right half, if any one return True
        return True  ##return True
    else:  ##if both return False, then else, pop it and return False
        arr.pop()
        return False
        
get_path(node,arr,target)
    