class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteK(head,k):
    current = head
    count = 1
    prev = None
    
    while current is not None:

        if count == k:
            prev.next = prev.next.next ##found so break out 
            break
        count +=1
        prev = current  ## else keep the prev in track
        current = current.next ##move the curr
        
    return head
    
    
    