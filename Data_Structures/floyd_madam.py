class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __int__(self):
        self.head=None
    def detectandremoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        s=self.head
        f=self.head
        while(s and f and f.next):
            s=s.next
            f=f.next.next
            #if slow and fast meet at same pt
            if s==f:
                print("Meeting point:",s.data)
                s=self.head
                while s.next!=f.next:
                    s=s.next
                    f=f.next
                print("Start of loop",f.next.data)
                f.next=None #remove loop
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
llist=LL()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)
#create a loop for testing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist.printlist()
llist.detectandremoveloop()
print("Linked list after remving loop")
llist.printlist()