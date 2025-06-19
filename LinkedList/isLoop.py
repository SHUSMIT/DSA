class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_loop(head):
    
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: ##if both stand/cross
            return True
    
    return False