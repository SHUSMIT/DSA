class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def sort012(head):
    #create 3 dummy nodes
    zero = Node(-1)
    one = Node(-1)
    two = Node(-1)
    
    #point the cureent to each of the node
    current0 = zero
    current1 = one
    current2 = two
    
    current = head
    
    while current is not None:
        
        #update the current in each of the cases. the common update of current is after all check
        
        if current.data == 0:
            current0.next = current
            current0 = current
        
        if current.data == 1:
            current1.next = current
            current1 = current
        
        if current.data == 2:
            current2.next = current
            current2 = current
        
        current = current.next
    
    #move the dummy
    
    zero = zero.next
    one = one.next
    two = two.next
    
    current0.next = one.next if one.next else two.next
    current1.next = two.next
    current2.next = None
    
    return zero.next if zero.next else (one.next if one.next else two.next)

