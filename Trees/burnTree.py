class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
from collections import deque

def parentnmap(node,parent):
    q = deque()
    q.append(node)
    parent[node] = None
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
            parent[node.left] = node
        if node.right:
            q.append(node)
            parent[node.right] = node

def timeburn(node,k):
    parent = {}
    parentnmap(node,parent)
    visited = set()
    
    q = deque()
    q.append(node)
    visited.add(node)
    time = 0
    
    while q:
        
        size = len(q)
        burn = False
        
        for _ in range(size):
            node = q.popleft()
            for neighbour in (node.left,node.right,parent[node]):
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
                    burn = True
        if  burn:            
            time += 1
    
    return time
    
    
    