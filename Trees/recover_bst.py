class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def swap(node1, node2):
    node1.val, node2.val = node2.val, node1.val

def inorder(root, arr, prev):
    if root is None:
        return
    inorder(root.left, arr, prev)
    if prev[0] and prev[0].val > root.val:
        if arr[0] is None:
            arr[0] = prev[0]
            arr[1] = root
        else:
            arr[2] = root
    prev[0] = root
    inorder(root.right, arr, prev)

def recover_bst(root):
    arr = [None, None, None]  # first, middle, last
    prev = [None]
    inorder(root, arr, prev)
    if arr[0] and arr[2]:
        swap(arr[0], arr[2])  # Non-adjacent nodes swapped
    elif arr[0] and arr[1]:
        swap(arr[0], arr[1])  # Adjacent nodes swapped
    # else: BST is already valid
    return root
