# x = [5]
# x.insert(0,6)
# x.insert(0,7)
# x.insert(0,8)
# print(x)
# x.pop(0)
# print(x)
try:
    x = int(input("enter age"))
    # y = int(input())
    # z = x/y
    # print(z)
    if(x<0):
        raise Exception("age cannot be negative")
except Exception as e:
    print("!!!Error:",e)
