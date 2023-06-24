class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            newnode=Node(data)
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
            self.head=newnode
        print("Data inserted Successfully")
        print("Insert at begin operation completed successfully")

    def insert_at_index(self,data,index):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            newnode=Node(data)
            count=0
            temp=self.head
            if index==0:
                newnode.next=self.head
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                self.head=newnode
                temp.next=self.head
                print('Data inserted successfully')
            else:
                while (index-1)!=count and temp is not None:
                    temp=temp.next
                    count+=1
                if temp==None:
                    print("Index out of range")
                else:
                    newnode.next=temp.next
                    temp.next=newnode
                    print('Data inserted successfully')
            print('Insert at index operation completed successfully')

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=Node(data)
            temp.next.next=self.head
        print("Data inserted Successfull")
        print("Insert at end operations completed successfully")
    
    def rotate(self,num):
        if self.head is None:
            print("List is empty")
        else:
            for i in range(num):
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                self.head=temp
        print("Rotate operation completed successfully")
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head.next
            print(self.head.data,end=' ')
            if self.head.next!=self.head:
                print('->',end=' ')
            while temp!=self.head:
                print(temp.data,end=' ')
                if temp.next!=self.head:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")

print("""1.Insert at Begin\n2.Insert at Index\n3.Insert at End
4.Rotate\n5.Display\n6.Exit\n""")
o=CSL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to insert at begin:"))
        o.insert_at_begin(data)
    elif ch==2:
        index=int(input("Enter index position:"))
        data=int(input("Enter Data to insert at given index:"))
        o.insert_at_index(data,index)
    elif ch==3:
        data=int(input("Enter Data to insert at end:"))
        o.insert_at_end(data)
    elif ch==4:
        num=int(input("Enter Number of time you want to rotate:"))
        o.rotate(num)
    elif ch==5:
        o.display()
    elif ch==6:
        print('\n\t********Your Exited********\n\t\t**THE END**\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")