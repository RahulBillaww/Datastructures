def push():
    n=int(input("enter the element to be inserted:"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,"is inserted into stack")
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"is deleted")
        del stack[0]

def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("elements of stack are:")
        for ele in stack:
            print(ele)
        print("Top of the stack is",stack[0])       
stack=list()
while(1):
    print("enter the operation from below\n 1.Push\n 2.Pop\n 3.Display\n enter any key to exit")
    str=input()
    if str=='1':
        print("PUSH OPERATION")
        push()
    elif str=='2':
        print("POP OPERATION")
        pop()
    elif str=='3':
        print("DISPLAYING ELEMENTS")
        display()
    else:
        print("EXIT FROM PROGRAM")
        break