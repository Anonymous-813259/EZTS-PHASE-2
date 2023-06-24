class circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.rear=-1
        self.front=-1

    def enqueue(self,data):
        if (self.rear+1)%self.size==self.front:
            print("Queue is Full")
        elif self.front==-1:
            self.rear=0
            self.front=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
        print("Enqueue operation completed successfully")
    
    def dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
        else:
            print("Deleted Element is: ",self.queue[self.front])
            if self.rear==self.front:
                self.rear=-1
                self.front=-1
            else:
                self.front=(self.front+1)%self.size

    def display(self):
        if self.front==-1:
            print("Queue is Empty")
            return
        temp=self.front
        print("Circular Queue Elements are: ",end=' ')
        while temp!=self.rear:
            print(self.queue[temp],end='->')
            temp=(temp+1)%self.size
        print(self.queue[temp])

queue=circularqueue(int(input("Enter size of queue:")))
while True:
    print("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        data=int(input("Enter data to insert:"))
        queue.enqueue(data)
    elif ch==2:
        queue.dequeue()
    elif ch==3:
        queue.display()
    elif ch==4:
        print("\n\t**THE END**\n")
        break
    else:
        print("\n\tInvalid Choice\nTRY ONCE AGAIN\n")