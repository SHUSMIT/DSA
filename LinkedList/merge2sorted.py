class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge2sorted(head1,head2):
    t1 = head1
    t2 = head2
    dummy = Node(-1)
    temp = dummy
    
    while t1 and t2:
        if t1.data >= t2.data:
            temp.next = t2  ## t1 is greater
            t2 = t2.next
        else:
            temp.next = t1
            t1 = t1.next
        temp = temp.next
    
    if t1:
        temp.next = t1
    else:
        temp.next = t2
    
    return dummy.next
    
