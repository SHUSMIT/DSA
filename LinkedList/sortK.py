class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

import heapq

def sortk(arr):
    pq = [] #make empty priority quue
    for node in arr:
        if node:
            heapq.heappush(pq, (node.data,node) )  ##priority queue has (val,node)
        
    dummy = Node(-1)
    temp = dummy
    
    while (pq):
        data,node = heapq.heappop(pq)  ##pop the min as per data
        temp.next = node ## join the temp with node
        temp = temp.next ##Move
        if node.next:  ##if the node has next
            heapq.heappush(pq , (node.next.data, node.next))  ##push it back
    
    return dummy.next
            
    