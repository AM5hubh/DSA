from queue import Queue


class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

def printtree(root,l1= None):
    if l1 is None:
        l1=[]
        l1.append(root)
    x = l1.pop(0)
    print(x.data)


# def printtree(root,level = 0):
#     # using recursion
#     # print(root.data)
#     for i in root.children:
#         printtree(i,level+1)
    # if len(root.children):
    #     for i in root.children:
    #         print(i.data)
    #         for j in i.children:
    #             printtree(j)




    # using queue
    # q = Queue()
    # q.put(root)
    # while not q.empty() :
    #     r = q.get()
    #     print(r.data)
    #     for i in r.children :
    #         q.put(i)



    # print(root.data)
    #
    # if len(root.children):
    #     for i in root.children:
    #         printtree(i)





n1 =Node(5)
n1.children.append(Node(10))
n1.children.append(Node(15))
n1.children[0].children.append(Node(20))
n1.children[0].children.append(Node(30))
n1.children[1].children.append(Node(40))
n1.children[1].children.append(Node(50))
printtree(n1)
# print(n1.__dict__)
# print(n1.data)
# print(n1.children[0].__dict__)
# print(n1.children[0].data)
# print(n1.children[0].children[0].__dict__)
# print(n1.children[0].children[0].data)
# n2 =Node(6)
# n3 =Node(7)
# n4 =Node(8)
# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)