class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def tortoise_hare(head):
    slow = head
    fast = head.next ## to get m1
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
    
def merge(left_head,right_head):
    dummy = Node(-1)
    temp = dummy
    while left_head and right_head:
        if left_head.data >= right_head.data:
            temp.next = right_head
            right_head = right_head.next # move it
        else:
            temp.next = left_head
            left_head = left_head.next
        temp = temp.next
    
    if left_head:
        temp.next = left_head
    if right_head:
        temp.next = right_head
    
    return dummy.next
    
def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle = tortoise_hare(head)
    left = head
    right = middle.next
    middle.next = None ## break/divide into two halves
    
    left_sort = merge_sort(left)
    right_sort = merge_sort(right)
    
    return merge(left_sort,right_sort)
    
