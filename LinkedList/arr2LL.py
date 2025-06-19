class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def arr2LL(arr):
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])  ##create a node
        current.next = temp ## current now points to temp
        current = current.next ##current moves to next
    return head

def printer(head):
    current = head
    while current is not None:
        print(current.data, end='->')
        current = current.next
    print('None')
    
arr = [1,2,3,4,56,57]
LL = arr2LL(arr)
printer(LL)