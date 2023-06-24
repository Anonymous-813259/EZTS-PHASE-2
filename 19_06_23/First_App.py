n=int(input("Enter Total Arr Size:"))
arr=list(map(int,input("Enter Numbers by separating them by space:").split()))
print("Your Arr:",arr)
print("1.Insert\n2.Delete\n3.Sort\n4.Search\n5.Exit")
while(True):
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        if len(arr)==n:
            print("Size is full")
        else:
            size=int(input("How many numbers do you want to insert:"))
            if len(arr)+size>n:
                print("Size out of range")
            else:
                arr=arr+list(map(int,input("Enter Number by seperating space:").split()))
                print("Your Arr:",arr)
    elif ch==2:
        if len(arr)==0:
            print("Array is empty")
        else:
            num=int(input("Enter Number to delete:"))
            n=len(arr)
            if num in arr:
                arr.remove(num)
            print("Your arr:",arr)
    elif ch==3:
        arr.sort()
        print("Your Arr:",arr)
    elif ch==4:
        search=int(input("Enter Number to search:"))
        n=0
        for i in range(len(arr)):
            if arr[i]==search:
                print("Element Found at position:",i+1)
                n=1
        if n==0:
            print("Element Not Found")
    elif ch==5:
        print("Your Exited\nTHE END")
        break
    else:
        print("Wrong Choice\nTry Once Again")