class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def detect(self):
        slow_p=self.head
        fast_p=self.head
        meet=None
        start=None
        while (slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                meet=slow_p
                break
        if meet is None:
            print("No Cycle")
        else:
            print(meet.data,"is meeting point")
            fast_p=self.head
            while slow_p != fast_p:
                slow_p=slow_p.next
                fast_p=fast_p.next
            start=slow_p
            print("Start of Cycle: ",start.data)
            while slow_p.next != start:
                slow_p=slow_p.next
            slow_p.next=None
        print("Done")
    
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

o=LL()
o.head=Node(1)
o.head.next=Node(2)
o.head.next.next=Node(3)
o.head.next.next.next=Node(4)
o.head.next.next.next.next=Node(5)
o.head.next.next.next.next.next=Node(6)
o.head.next.next.next.next.next.next=Node(7)
o.head.next.next.next.next.next.next.next=Node(8)
o.head.next.next.next.next.next.next.next.next=Node(9)
o.head.next.next.next.next.next.next.next.next.next=o.head.next.next.next
o.detect()
#o.display()