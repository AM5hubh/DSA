class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sub = None

class Linkedlist:

    def __init__(self):
        self.head = None



    def delfirstnode(self):
        if(not self.head):
            print("Linkedlist is empty")
        else:
            t = self.head
            self.head = self.head.next
            t.next = None

    def dellastnode(self):
        if self.head == None:
            print("Linkedlist is empty")
        elif(self.head.next == None):
            self.head = None
        else:
            t = self.head
            while t.next.next:
                t = t.next
            t.next=None

    def delanynode(self):
        delnode = int(input("Enter the node index"))
        if(self.head == None):
            print("Linkedlist is empty")
        else:
            t = self.head
            i = 1
            while(delnode >2):
                t = t.next
                delnode -= 1
            t1 = t.next
            t.next = t1.next
            t1.next = None


    def bubbleSort(self):
        length = self.length()

        while(length > 1):
            t1 = self.head
            i=1
            while(i<length):
                if(t1.data>t1.next.data):
                    tmp = t1.data
                    t1.data = t1.next.data
                    t1.next.data = tmp
                t1 = t1.next
                i+=1
            length -= 1
        print("After bubblesort")


    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        # print("None")

    def length(self):
        t = self.head
        i = 0
        while t:
            i+=1
            t = t.next
        return i
        # pass

    def reverselist(self):
        t = self.head
        while(t):
            print(t.data)
            t = t.next

    def append(self):
        if not self.head:
            self.head = Node(int(input("Enter no.")))
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(int(input("Enter no.")))

    def subpointer(self):
        # self.sub = None
        pos = int(input("Enter index pos to add sub."))
        if (self.head == None):
            print("Linkedlist is empty")
        elif(pos < 0 or pos > self.length()):
            print("Index out of range")
        else:
            t = self.head
            i = 1
            while(i<pos):
                t = t.next
                i+=1
            if(hasattr(t,"sub")==False):
                # t.sub = Linkedlist().append()
                n = t.data
                i = 2
                while(i<=10):
                    print(i)
                    if(i==2):
                        t.sub = Node(n*i)
                        t = t.sub
                    else:
                        t.next = Node(n*i)
                        t = t.next
                    i+=1

l1 = Linkedlist()
l1.append()
l1.append()
l1.append()
l1.append()
l1.append()
l1.append()
l1.subpointer()
#
t = l1.head
i = 1
while(i<=10):
    print(t.sub.data)
    if(i==1):
        t = t.sub
    else:
        t=t.next
    i+=1
# l1.bubbleSort()
# l1.display()
# l1.reverselist()
# l1.delanynode()
# l1.display()
# l1.dellastnode()
# l1.delfirstnode()
