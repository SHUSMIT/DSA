class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

import heapq

def vertical(node):
    pq = []
    
    ## priority queue (x_ordi, level, node) where samllest from left wise pops
    
    heapq.heappush(pq , (0, 0, node))
    vertical_travel = []

    while pq:
        
        x_ordi,level,node = heapq.heappop(pq)
        
        if node.left:
            # For left child: x_ordi - 1, level + 1
            heapq.heappush(pq, (x_ordi - 1, level + 1, node.left))
        if node.right:
            # For right child: x_ordi + 1, level + 1
            heapq.heappush(pq, (x_ordi + 1, level + 1, node.right))
            
        vertical_travel.append(node.data)
    
        
        