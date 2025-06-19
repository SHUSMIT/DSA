class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def inorder_postorder(in_start,in_end,inorder,post_start,post_end,postorder,inmap):
    
    if in_start > in_end or post_start > post_end:
        return None  ## base,leaf condition
    
    root = Node(postorder[post_end])  ## the first of any pre order is the root
    inorder_index = inmap[postorder[post_end]] ## get the value of index of inorder first element,ie,root
    size_left = inorder_index - in_start  ## this is the left size computed from inorder. see dry run 
    
    ## do a dry run to understand the index placing 
    
    root.left = inorder_postorder(in_start , inorder_index-1 ,inorder , post_start , post_start + size_left ,inmap)  ## recursively do for left half
    root.right = inorder_postorder(inorder_index+1 , in_end ,post_start+size_left+1,post_end-1,inmap) ##recursively do for right half
    
    return root
    
    

def construct(inorder,postorder):
    inmap = {}
    map_inorder(inmap,inorder)  ## inorder means left,root,right and preorder is root,left,right
    
    in_start = 0
    in_end = len(inorder) - 1
    post_start = 0
    post_end = len(postorder) - 1
    
    root = inorder_postorder(in_start,in_end,inorder,post_start,post_end,postorder,inmap)
    
    return root
    
    
def map_inorder(inmap,inorder):
    for idx in range(len(inorder)):
        inmap[inorder[idx]] = idx ## inorder array node , index 
    
    