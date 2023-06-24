class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

def preoder(root):
    if root:
        print(root.key,end=' ')
        preoder(root.left)
        preoder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=' ')

root=Node(100)
root.left=Node(400)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right=Node(500)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("Inoder Traversal:- ",end=' ')
inorder(root)
print()
print("Preoder Traversal:- ",end=' ')
preoder(root)
print()
print("Postorder Traversal:- ",end=' ')
postorder(root)
print()
print("\t**THE END**")