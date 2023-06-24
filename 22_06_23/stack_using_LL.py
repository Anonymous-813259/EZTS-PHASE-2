class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def push_begin(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
        print("Data inserted Successfully")
        print("Insert at begin operation completed successfully")

    def pop_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at Begin operation is completed successfully")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")

print("""1.Push\n2.Pop\n3.Display\n4.Exit\n""")
o=SLL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to push:"))
        o.push_begin(data)
    elif ch==2:
        o.pop_begin()
    elif ch==3:
        o.display()
    elif ch==4:
        print('\n\t********Your Exited********\n\t\t**THE END**\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")