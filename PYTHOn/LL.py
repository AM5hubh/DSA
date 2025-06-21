class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,numberstoadd):

        for i in range(numberstoadd):
            if self.head == None:
                self.head = Node(int(input("Enter the data: ")))
            else:
                p = self.head
                while p.next:
                    p = p.next
                p.next = Node(int(input("Enter the data: ")))


    def displaydata(self):
        if(self.head == None):
            print("Linkedlist is empty")
        else:
            p = self.head
            while p:
                print(p.data,end = " ")
                p = p.next
            print()

    def findandreturnindex(self):
        number = int(input("Enter the number: "))
        if(self.head == None):
            print("Linkedlist is empty")
        else:
            p = self.head
            i = 1
            while p:
                if(p.data == number):
                    print(i)
                p = p.next
                i+=1

    def deletefirst(self):
        if(self.head == None):
            print("Linkedlist is empty")
        else:
            p = self.head.next
            self.head = None
            self.head = p

    def deletelast(self):
        if(self.head == None):
            print("Linkedlist is empty")
        elif(self.head.next == None):
            self.head = None
        else:
            p = self.head
            while(p.next.next):
                p = p.next
            p.next = None

    def delanyndata(self):
        nodeindex = int(input("Enter the index of the node to be deleted: "))
        if(self.head == None):
            print("Linkedlist is empty")
        else:
            p = self.head
            if(nodeindex == 1):
                self.deletefirst()

ll = LinkedList()
ll.append(int(input("Enter the numbers to add:")))
ll.displaydata()
# ll.deletefirst()
# ll.deletelast()
ll.delanyndata()
ll.displaydata()

# ll.findandreturnindex()