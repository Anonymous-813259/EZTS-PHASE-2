class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None

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
current=root
stack=[]
while True:
    if current:
        stack.append(current)
        current=current.left
    elif stack:
        current=stack.pop()
        print(current.key,end=' ')
        current=current.right
    else:
        break
print()
print("Preoder Traversal:- ",end=' ')
current=root
stack=[]
while True:
    if current:
        print(current.key,end=' ')
        stack.append(current)
        current=current.left
    elif stack:
        current=stack.pop()
        current=current.right
    else:
        break
print()
'''print("Postorder Traversal:- ",end=' ')
while True:
    if current:
        stack.append(current)
        current=current.left
    elif stack:
        current=stack.pop()
        current=current.right
        print(current.key,end=' ')
    else:
        break'''
print("\n\t\t\t**THE END**")