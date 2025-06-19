class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque        
def zigzag(node,zig):
    q = deque()
    q.append(node)
    left_right = 1 ## 1 is left to right, 0 is right to left
    zig = []
    
    while q:
        ##keep a level and level_size
        level = []
        level_size = len(q)  ## only after a certain node is popped additonal nodes can be pushed so leveln size
        
        for _ in range(level_size):
            
            node = q.popleft()  ##keep popping till the length
            
            ## add left and right into the queue
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            level.append(node.data)  ## add it to an level list
            
        if left_right:  ## if left right, then directly add
            zig.extend(level)
        else:  ## else reverse and then add
            level.reverse()
            zig.extend(level)
        
        left_right = not left_right 
            
            