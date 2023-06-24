class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        if self.rear is None:
            self.rear=Node(data)
            self.front=self.rear
        else:
            newnode=Node(data)
            self.rear.next=newnode
            self.rear=newnode
        print("Data inserted Successfully")
        print("Enqueue operation completed successfully")

    def dequeue(self):
        if self.front is None:
            print("List is empty")
        else:
            temp=self.front
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Dequeue operation is completed successfully")

    def display(self):
        if self.front is None:
            print("List is empty")
        else:
            temp=self.front
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('<-',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")

print("""1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n""")
o=SLL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to push:"))
        o.enqueue(data)
    elif ch==2:
        o.dequeue()
    elif ch==3:
        o.display()
    elif ch==4:
        print('\n\t********Your Exited********\n\t\t**THE END**\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")