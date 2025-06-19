class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindromme(head):
    
    if head is None or head.next is None:
        return True
    ##for comparison
    first = head
    
    slow = head
    fast = head
    
    while(fast.next is not None and fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    newHead = reverseLL(slow.next)
    second = newHead
    
    while slow is not None:
        if first.data != second.data:
            reverseLL(newHead)  ## good practice
            return False
        first = first.next
        second = second.next
    
    reverseLL(newHead)
    return True
    
    

# def reversal(head):
#     current = head
#     prev = None
    
#     while current is not None:
#         front = current.next  ##keep a record of front
        
#         current.next = prev ## make link change
        
#         prev = current  ##move prev 
#         current = front #move current
    
#     return prev

# def tortoiseANDhare(head,slow):
#     current = head
#     slow = head
#     fast = head
    
#     odd = False
#     even = False
    
#     while(fast.next.next is not None and fast.next is not None):
        
#         fast.next = current.next.next
#         slow.next = current.next
#         current = current.next
        
#         if fast.next is None:
#             odd = True
#         if fast.next.next is None:
#             even = True
    
#     return (odd,even,slow)

# def isPalindromme(head):
    
#     first = head
#     odd,even,slow = tortoiseANDhare(head,-1)
    
#     if odd: ## then slow will be at the middle, we reverse slow.next and move the two pointer such that first end as slow
#         second = reversal(slow.next)
        
#         while first is not slow:
#             if first.data != second.data:
#                 return False
            
#             ##move both now
#             first = first.next 
#             second = second.next
    
#     else:
#         second = reversal(slow.next)
        
#         while first is slow:
#             if first.data != second.data:
#                 return False
            
#             ## move both now
#             first = first.next
#             second = second.next
    
#     return True
            
       
# def reverseLL(head):
#     temp = head
#     prev = None
#     while temp is not None:
#         front = temp.next
#         temp.next = prev
#         prev = temp
#         temp = front
    
#     return prev
