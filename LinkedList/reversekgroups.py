class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def knode(temp,k):
    count = 1
    while count != k:
        temp = temp.next
        count += 1
    return temp

def reverse(head):
    
    temp = head
    prev = None
    
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
    return prev

def reverseK(head,k):
    temp = head
    next_node = None
    prev_node = None
    
    while temp:
        
        k_node = knode(temp,k)  ## got the kth Node
        if k_node == None:
            if (prev_node):
                prev_node.next = temp
            break
        
        next_node = k_node.next   ## store the k_node.next else lost
        k_node.next = None ## break the linkage
        newHead = reverse(temp)
        
        if head == temp:
            head = newHead ## the first k group 
        
        else:
            prev_node.next = newHead ##connect prev_node with next_node
            
        prev_node = temp  ## now keep record of prev_node to connect above
        temp = next_node  ## move temp forward
        
    return head
        
        