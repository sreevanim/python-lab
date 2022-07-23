class Node:
    def __init__(self,dataval):
        self.dateval=dataval
        self.nextval=None
        print("Node created sucessfully\ndata in node is:",dataval)
class SLinkedList:
    def __init__(self):
        self.headval=None
list1=SLinkedList()
list1.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list1.headval.nextval=e2
e2.nextval=e3
