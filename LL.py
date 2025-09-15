class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=ne
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    def delete_at_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while(temp.next is not None):
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_at_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=SingleLinkedList()
n=Node(10)
L.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.n3xt=n4
L.insert_beginning(5)
L.insert_at_end(100)
L.insert_at_end(110)
L.insert_at_position(3,25)
L.insert_at_position(4,35)
L.insert_at_position(7,45)
L.insert_at_position(8,75)
L.insert_at_position(2,15)
L.delete_at_beginning()
L.delete_at_end()
L.delete_at_position(3)
L.display()