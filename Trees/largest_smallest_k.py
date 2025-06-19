class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def morris(node):
    cur = root
    '''
    if left doesnt exist, it is node, so add it ( inorder is left, root , right)
    else we move first left, we assign prev = curr.left. and then keep moving prev = prev.right. 
    once null reached, we point it to current ( which is the root )
    then in the if block of else, if right is Null and it doesnt point to itself ( not threaded) we point it to current
    move current left
    else
    we append the current,we point the right of prev to null ( already threaded ) and move curr to righ
    '''
    while cur:
        if not curr.left:
            arr.append(curr)
        else:
            
            prev = curr.left
            
            while prev.right and prev.right != curr:
                prev = prev.right
            
            if prev.right is None: ## reach end and not point
                prev.right = curr 
                curr = curr.left # continue moving
            else:
                prev.right = None
                arr.append(curr)
                curr = curr.right ## continue moving

        
def morris_kth_smalelst(node,k):
    curr = node
    count = 0
    while curr:
        if curr.left is None:
            count += 1
            if count == k:
                return curr.val
        else:
            prev = curr.left
            while prev.right and prev.right != curr: ## exist and not visited
                prev = prev.right ## keep moving right
                
            if prev.right is None:
                prev.right = curr ## thread
                curr = curr.left ## move left
            
            else:
                prev.right = None
                count +=1 
                if count == k:
                    return curr.val
                cur = curr.right ## move right
    
    return -1

## right becomes left, reverse inorder  
def morris_kth_largest(node, k):
    curr = node
    count = 0
    while curr:
        if curr.right is None:
            count += 1
            if count == k:
                return curr.val
            curr = curr.left
        else:
            prev = curr.right
            while prev.left and prev.left != curr:
                prev = prev.left
            if prev.left is None:
                prev.left = curr
                curr = curr.right
            else:
                prev.left = None
                count += 1
                if count == k:
                    return curr.val
                curr = curr.left
    return -1
         
def inorder_k_smalllest(node,k):
    count = 0
    while node:
        if node.left:
            count +=1 
            if count == k:
                return node.val
            node = node.left
        else:
            count += -1
            if count ==k:
                return node.val
            node = node.right

def inorder_k_largest(node,k):
    count = 0
    while node:
        if node.right:
            count +=1
            if count ==k:
                return node.val
            node = node.right
        else:
            count += 1
            if count ==k:
                return node.val
            node = node.left
        