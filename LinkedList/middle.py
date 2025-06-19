class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def middle(head):
    slow,fast = head,head
    ##move both simultaneosly, when null reached, move to oppossite head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow