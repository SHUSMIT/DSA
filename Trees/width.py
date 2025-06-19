class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

from collections import deque

def width(node):
    if not node:
        return None
    
    q = deque()  ## create a queue 
    width = 0 ## difference of left and right
    q.append((node,0)) # store node,i
    
    while q:
        size = len(q)
        _,first = q[0]  ## first index of q at given level
        -,last = q[-1]  ## last index of q at given level
        width = max(width, last - fast + 1)
        
        for _ in range(size): ## pop all in that level
            node,index = q.popleft()
            index -= first ## normalise it subtract the min of level
            if node.left:
                q.append((node.left, 2*index + 1 ))
            if node.right:
                q.append((node.right, 2*index + 2 ))
        
    return width
            
                
    