class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BST_next_Iterator:
    def __init__(self, node):
        self.stack = []
        self.add(node)

    def add(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        val = node.val
        if node.right:
            self.add(node.right)
        return val

class BST_before_iterator:
    def __init__(self, node):
        self.stack = []
        self.add(node)

    def add(self, node):
        while node:
            self.stack.append(node)
            node = node.right

    def before(self):
        if not self.stack:
            return None
        node = self.stack.pop()
        val = node.val
        if node.left:
            self.add(node.left)
        return val

def two_sum(node, k):
    left_iter = BST_next_Iterator(node)
    right_iter = BST_before_iterator(node)
    
    left_val = left_iter.next()
    right_val = right_iter.before()
    
    while left_val is not None and right_val is not None and left_val < right_val:
        if left_val + right_val == k:
            return (left_val, right_val)
        elif left_val + right_val < k:
            left_val = left_iter.next()
        else:
            right_val = right_iter.before()
    return None

