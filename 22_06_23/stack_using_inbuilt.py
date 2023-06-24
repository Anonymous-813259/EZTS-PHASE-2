from queue import LifoQueue

obj=LifoQueue(maxsize=3)
#put -> push
obj.put('a')
obj.put('b')
obj.put('c')
#get -> pop and full -> isfull 
print(obj.full())
print(obj.qsize())
print(obj.get())
print(obj.qsize())
print(obj.get())
print(obj.get())
print(obj.empty())