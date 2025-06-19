class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_loop(head):
    count = 0
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast: ##if both stand/cross
        
            #move fast one step and counter increase
            fast = fast.next
            count += 1
            
            while slow != fast:
                fast = fast.next
                count +=1
                
            return count
    
    return -1