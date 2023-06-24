queue=[]
def enqueue(data):
    queue.append(data)
    while True:
        ch=input("Do you want to see the queue(Y/N):")
        if ch=='Y':
            print(queue)
            break
        elif ch=='N':
            break
        else:
            print("Enter correct Option")

def dequeue():
    if not queue:
        print("queue is empty")
        return
    print(queue[-1],"is poped")
    queue.pop(0)
    while True:
        ch=input("Do you want to see the queue(Y/N):")
        if ch=='Y':
            print(queue)
            break
        elif ch=='N':
            break
        else:
            print("Enter correct Option")

def show():
    print("queue elements are: ",queue)

while True:
    ch=int(input("""1.Push\n2.Pop\n3.Display\n4.Seek\n5.Quit\nEnter Your Choice:"""))
    if ch==1:
        data=int(input("Enter Your Data:"))
        enqueue(data)
    elif ch==2:
        dequeue()
    elif ch==3:
        show()
    elif ch==4:
        if not queue:
            print("queue is Empty")
        else:
            data=int(input("Enter Search element:"))
            if data not in queue:
                print(data,"is not in queue")
            else:
                print(data,"is at index:",queue.index(data))
    elif ch==5:
        print("\nThank You For Using\n\tTHE END")
        break
    else:
        print("Enter correct Option")