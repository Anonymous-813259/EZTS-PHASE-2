stack=[]
def push(data):
    stack.append(data)
    while True:
        ch=input("Do you want to see the stack(Y/N):")
        if ch=='Y':
            print(stack)
            break
        elif ch=='N':
            break
        else:
            print("Enter correct Option")

def pop_element():
    if not stack:
        print("Stack is empty")
        return
    print(stack[-1],"is poped")
    stack.pop()
    while True:
        ch=input("Do you want to see the stack(Y/N):")
        if ch=='Y':
            print(stack)
            break
        elif ch=='N':
            break
        else:
            print("Enter correct Option")

def show():
    print("Stack elements are: ",stack)

def even_odd(ch):
    if ch=='1':
        print("Even Numbers: ",end=' ')
        for i in stack:
            if i%2==0:
                print(i,end=' ')
        print()
    elif ch=='2':
        print("Odd Numbers: ",end=' ')
        for i in stack:
            if i%2!=0:
                print(i,end=' ')
        print()
    else:
        print("Invalid Entry")

while True:
    ch=int(input("""1.Push\n2.Pop\n3.Display\n4.Peek/Top\n5.Seek\n6.Even or Odd display\n7.Quit\nEnter Your Choice:"""))
    if ch==1:
        data=int(input("Enter Your Data:"))
        push(data)
    elif ch==2:
        pop_element()
    elif ch==3:
        show()
    elif ch==4:
        if not stack:
            print("Stack is Empty")
        else:
            print("Top of the stack:",stack[-1])
    elif ch==5:
        if not stack:
            print("Stack is Empty")
        else:
            data=int(input("Enter Search element:"))
            if data not in stack:
                print(data,"is not in stack")
            else:
                print(data,"is at index:",stack.index(data))
    elif ch==6:
        c=input("Do you want to see the even or odd(1 for Even/2 for Odd):")
        even_odd(c)
    elif ch==7:
        print("Thank You For Using\n\tTHE END")
        break
    else:
        print("Enter correct Option")