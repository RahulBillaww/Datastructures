class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        x=int(input("enter element to be inserted"))
        new=Node(x)
        if self.front is None:
            self.front=new
            self.rear=new
        else:
            self.rear.next=new
            self.rear=new
    def dequeue(self):
        if  self.front is None:
            print("QUEUE IS EMPTY")
        elif self.front.next is None:
            print("Popped element is ",self.front.data)
            self.front=None
        else:
            temp=self.front
            print("Popped element is ",self.front.data)
            self.front=temp.next
            temp=None
    def display(self):
        if self.front is None:
            print("QUEUE IS EMPTY")
        else:
            temp=self.front
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
            print("\nFRONT OF QUEUE IS",self.front.data)
            print("REAR OF QUEUE IS",self.rear.data)
q=Queue()
while(1):
    print("enter the operation from below\n 1.ENQUEUE\n 2.DEQUEUE\n 3.Display\n enter any key to exit")
    str=input()
    if str=='1':
        print("ENQUEUE OPERATION")
        q.enqueue()
    elif str=='2':
        print("DEQUEUE OPERATION")
        q.dequeue()
    elif str=='3':
        print("DISPLAYING ELEMENTS")
        q.display()
    else:
        print("EXIT FROM PROGRAM")
        break