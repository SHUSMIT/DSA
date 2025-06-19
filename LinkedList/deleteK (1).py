class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteK(head,k):
    fast = head
    slow = head
    for _ in range(k):
        fast = fast.next ## move the fast k steps ahead 
        
    if fast is None: ## end reached, head to be removed
        return head.next
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next ## when fast reaches the end, slow is k steps from end as per condition
        
    slow.next = slow.next.next
    
    return head