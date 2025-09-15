class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("CLL IS EMPTY")
            return
        else:
            temp = self.head
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

    def insert_at_beginning(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new.next = self.head
            self.head = new
            self.tail.next = new  
            


# Test the code
L = CLL()
L.insert_at_beginning(10)
L.insert_at_beginning(20)
L.insert_at_beginning(30)
L.display()
