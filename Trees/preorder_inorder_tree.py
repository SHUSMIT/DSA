class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def inorder_preorder(in_start,in_end,inorder,pre_start,pre_end,preorder,inmap):
    
    if in_start > in_end or pre_start > pre_end:
        return None  ## base,leaf condition
    
    root = Node(preorder[pre_start])  ## the first of any pre order is the root
    inorder_index = inmap[preorder[pre_start]] ## get the value of index of inorder first element,ie,root
    size_left = inorder_index - in_start  ## this is the left size computed from inorder. see dry run 
    
    ## do a dry run to understand the index placing 
    
    root.left = inorder_preorder(in_start,inorder_index-1,inorder,pre_start+1,pre_start+size_left,inmap)  ## recursively do for left half
    root.right = inorder_preorder(inorder_index+1,in_end,pre_start+size_left+1,pre_end,inmap) ##recursively do for right half
    
    return root
    
    

def construct(inorder,preorder):
    inmap = {}
    map_inorder(inmap,inorder)  ## inorder means left,root,right and preorder is root,left,right
    
    in_start = 0
    in_end = len(inorder) - 1
    pre_start = 0
    pre_end = len(preorder) - 1
    
    root = inorder_preorder(in_start,in_end,inorder,pre_start,pre_end,preorder,inmap)
    
    return root
    
    
def map_inorder(inmap,inorder):
    for idx in range(len(inorder)):
        inmap[inorder[idx]] = idx ## inorder array node , index 
    
    