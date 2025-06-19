class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def y_intersect(head1,head2):
    temp1,temp2 = head1,head2
    ##move both simultaneosly, when null reached, move to oppossite head
    while temp1 != temp2:
        temp1 = temp1.next if temp1 else None
        temp2 = temp2.next if temp2 else None
    
    return temp1 