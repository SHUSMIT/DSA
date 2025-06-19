class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
from collections import deque

def parentmap(node,parent):
    q = deque()
    q.append(node)
    parent[node] = None ## root node has no parent
    ##simple bfs traversal
    while q:
        node = q.popleft()
        if node.left: ##left exist
            parent[node.left] = node
            q.append(node.left)
        if node.right:
            parent[node.right] = node
            q.append(node.right)

def print_node_k(node,k):
    parent = {}
    parentmap(node,parent) ##to get the parent of each
    
    visited = set() ## keep a track of visted, set for fast and unique node ( node stored so always unique only)
    q = deque() ## use queue for traversal
    
    q.append(node)
    visited.add(node)
    distance = 0
    
    while q:
        level_size = len(q)  ## to get level size
        if distance == k:
            return [n for n in q] ## return entire q if dist == k
        
        for _ in range(level_size):
            node = q.popleft()  ## check left,neghbour and parent... if not visited only then push into q. and distance ++ 
            
            for neighbour in (node.left, node.right, parent[node]):
                if neighbour and neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour) ## add to visited
            
        distance += 1
            
            
            