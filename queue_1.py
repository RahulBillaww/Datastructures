def enqueue():
    n=int(input("enter the elementto be inserted"))
    queue.append(n)
    print()

def dequeue():
    if len(queue)==0:
        print("QUEUE IS EMPTY")
    else:
        print(queue[0],"is the deleted element")
        del queue[0]
        print()

def display():
    if len(queue)==0:
        print("QUEUE IS EMPTY")
    else:
        print("ELEMENTS IN THE QUEUE ARE:")
        for ele in queue:
            print(ele, end=" ")
        print("\nFRONT OF THE QUEUE IS",queue[0])
        print("REAR OF THE QUEUE IS",queue[-1])

queue=list()
while(1):
    print("enter the operation from below\n 1.ENQUEUE\n 2.DEQUEUE\n 3.Display\n enter any key to exit")
    str=input()
    if str=='1':
        print("ENQUEUE OPERATION")
        enqueue()
    elif str=='2':
        print("DEQUEUE OPERATION")
        dequeue()
    elif str=='3':
        print("DISPLAYING ELEMENTS")
        display()
    else:
        print("EXIT FROM PROGRAM")
        break


        

