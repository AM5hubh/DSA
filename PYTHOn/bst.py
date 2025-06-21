class Node:
    def __init__(self, data,lp=None,rp=None):
        self.data = data
        self.lp = lp
        self.rp = rp


class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            p=self.root
            while p:
                if(data < p.data ):
                    if p.lp:
                        p = p.lp
                    else:
                        p.lp = Node(data)
                        break
                elif(data > p.data):
                    if p.rp:
                        p = p.rp
                    else:
                        p.rp = Node(data)
                        break


    def preOrderTraversal(self,root):
        if(root is None):
            return
        print(root.data)
        self.preOrderTraversal(root.lp)
        self.preOrderTraversal(root.rp)

t =BST()
t.insert(50)
t.insert(25)
t.insert(12)
t.insert(20)
t.preOrderTraversal(t.root)
# print(t.root.data)
# print(t.root.lp.data)
# print(t.root.lp.lp.data)
# print(t.root.lp.lp.rp.data)