class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        x=int(input("Enter element to be inserted:"))
        new=Node(x)
        if self.top is None:
            self.top=new
            new.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top is None:
            print("stack is empty")
        elif self.top.next is None:
            print("Popped element is",self.top.data)
            print("---------------------------")
            self.top=None
        else:
            temp=self.top
            print("Popped element is",self.top.data)
            print("---------------------------")
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Elements of stack:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of Stack is",self.top.data)
s=Stack()
while(1):
    print("enter the operation from below\n 1.Push\n 2.Pop\n 3.Display\n enter any key to exit")
    str=input()
    if str=='1':
        print("PUSH OPERATION")
        s.push()
    elif str=='2':
        print("POP OPERATION")
        s.pop()
    elif str=='3':
        print("DISPLAYING ELEMENTS")
        s.display()
    else:
        print("EXIT FROM PROGRAM")
        break
            