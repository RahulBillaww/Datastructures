class CircularQueue:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    def enqueue(self,item):
        if (self.rear+1)%self.size == self.front:
            print("Queue is Full")
        elif self.front==-1:
            self.front=self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item
    def dequeue(self):
        if self.front==-1:
            print("QUEUE IS EMPTY")
        elif self.front==self.rear:
            item=self.queue[self.front]
            self.front=self.rear=-1
            return item
        else:
            item=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return item
    def display(self):
        if self.front==-1:
            print("QUEUE IS EMPTY")
        else:
            i=self.front
            while True:
                print(self.queue[i],end=" ")
                if i==self.rear:
                    break
                i=(i+1)%self.size
        print()

cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()      
cq.dequeue()      
cq.enqueue(40)    
cq.display()      

        