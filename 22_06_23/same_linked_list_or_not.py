class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
        print("Data inserted Successfully")
        print("Insert at begin operation completed successfully")
    
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
            print()

class operation:
    #look after positions also
    def same_or_not(self,l1,l2):
        temp1=l1.head
        temp2=l2.head
        flag=0
        '''len_l1=0
        len_l2=0
        while temp1 is not None:
            len_l1+=1
            temp1=temp1.next
        while temp2 is not None:
            len_l2+=1
            temp2=temp2.next
        temp1=l1.head
        temp2=l2.head
        while temp1 is not None:
            temp2=l2.head
            while temp2 is not None:
                if temp1.data==temp2.data:
                    len_l1-=1
                    len_l2-=1
                temp2=temp2.next
            temp1=temp1.next
        if len_l1==0 and len_l2==0:
            print(True)
        else:
            print(False)'''
        temp1=l1.head
        temp2=l2.head
        while temp1 is not None and temp2 is not None:
            if temp1.data!=temp2.data:
                flag=1
                break
            temp1=temp1.next
            temp2=temp2.next
        if temp1 is None and temp2 is None and flag==0:
            print(True)
        else:
            print(False)

l1=SLL()
l2=SLL()
print("For first Linked List:")
while True:
    print("1.Insert at Begin\n2.Display List1\n3.Exit from List 1")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to insert at begin:"))
        l1.insert_at_begin(data)
        print()
    elif ch==2:
        l1.display()
        print()
    elif ch==3:
        print("THE END of List 1")
        print()
        break
    else:
        print("Invalid Entry")
        print()
while True:
    print("1.Insert at Begin\n2.Display\n3.Exit from List 2")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to insert at begin:"))
        l2.insert_at_begin(data)
        print()
    elif ch==2:
        l2.display()
        print()
    elif ch==3:
        print("THE END of List 1")
        print()
        break
    else:
        print("Invalid Entry")
        print()
op=operation()
print("List 1 Elements are:",end=' ')
l1.display()
print()
print("List 2 Elements are:",end=' ')
l2.display()
print()
op.same_or_not(l1,l2)