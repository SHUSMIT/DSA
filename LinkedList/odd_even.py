class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def oddEven(head):
    odd = head
    even = head.next
    even_head = even
    
    if head is None or head.next is None:
        return head
    
    while even and even.next:  ## odd,even,odd.next,even.next ---> so even bounds odd and even.next bound odd.next
        odd.next = odd.next.next
        even.next = even.next.next
        
        odd = odd.next
        even = even.next.next
    
    odd.next = even_head
    
    return odd
    
        
    
