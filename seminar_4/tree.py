class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(node, value):
    if node is None or node.data == value:
        return node
    
    if node.data > value:
        return search(node.left, value)
    else: search(node.right, value)
    

def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.data)
        print_tree(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(18)

node = search(root, 5)

if node:
    print(True)
else:
    print(False)

print_tree(root)