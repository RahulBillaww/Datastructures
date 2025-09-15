class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        nb=Node(data)
        temp=self.head
        temp.prev=nb
        nb.next=temp
        self.head=nb
    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=ne
        ne.prev=temp
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
    def delete_at_beginning(self):
        temp=self.head
        self.head=temp.next
        self.head.prev=None
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        temp.prev=None
        before.next=None
    def delete_at_position(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.prev=None
        temp.next=None
    def display(self):
        if self.head is None:
            print("DLL IS EMPTY")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=DLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n4.prev=n3
n3.next=n4
L.insert_at_beginning(8)
L.insert_at_beginning(5)
L.insert_at_end(50)
L.insert_at_end(60)
L.insert_at_position(5,25)
L.insert_at_position(6,28)
L.display()