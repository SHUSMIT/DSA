class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def bst_preorder(arr,idx,bound):
    if len(arr) < idx[0] or arr[idx[0]] > bound: ## bound exceed the ith value of arr or idx exceed len(arr)
        return None
    
    root = Node(arr[idx])
    idx[0] += 1
    
    root.left = bst_preorder(arr,idx,root.val)  ## for left, the bound would be root.val
    root.right = bst_preorder(arr,idx,bound)  ## for right the bound remains
    
    return root
    
bst_preorder(arr,0,float('inf'))
    
    
    