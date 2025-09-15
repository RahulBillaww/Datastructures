class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("CLL IS EMPTY")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
    def insert_at_beginning(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
            self.head=new
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
    def insert_at_position(self,pos,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            if pos==1:
                L.insert_at_beginning(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new.next=temp.next
                temp.next=new
    def delete_at_beginning(self):
        if self.head is None:
            print("No nodes in CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                self.head=temp.next
                temp=None
                self.tail.next=self.head
    def delete_at_end(self):
        if self.head is None:
            print("No nodes in CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                while temp.next!=self.tail:
                    temp=temp.next
                self.tail=None
                self.tail=temp
                temp.next=self.head
    def delete_at_pos(self,pos):
        if self.head is None:
            print("No nodes in CLL")
        elif pos==1:
            L.delete_at_beginning()
        else:
            temp1=self.head
            temp2=self.head.next
            for i in range(1,pos-1):
                temp1=temp1.next
                temp2=temp2.next
            temp1.next=temp2.next
            if(temp2==self.tail):
                self.tail=temp1
            temp2=None
    def Search(self):
        x=int(input("Enter the element to be searched:"))
        temp=self.head
        count=0
        flag=0
        while(temp!=self.tail):
            if x==temp.data:
                flag=1
                break
            temp=temp.next
            count=count+1
        else:
            if x==temp.data:
                flag=1
        if flag==1:
            print(x,"element is found at position",count+1)
        else:
            print(x,"is not found in CLL")    
L=CLL()
L.insert_at_beginning(10)
L.insert_at_beginning(20)
L.insert_at_end(40)
L.insert_at_position(3,30)
L.insert_at_position(5,50)
L.display()
L.Search()