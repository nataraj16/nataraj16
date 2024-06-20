class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            newnode=Node(data)
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
            self.head=newnode
        print("Data inserted Successfully")
        print("Insert at begin operation completed successfully")

    def insert_at_index(self,data,index):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            newnode=Node(data)
            count=0
            temp=self.head
            if index==0:
                newnode.next=self.head
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                self.head=newnode
                temp.next=self.head
                print('Data inserted successfully')
            else:
                while (index-1)!=count and temp is not None:
                    temp=temp.next
                    count+=1
                if temp==None:
                    print("Index out of range")
                else:
                    newnode.next=temp.next
                    temp.next=newnode
                    print('Data inserted successfully')
            print('Insert at index operation completed successfully')

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=Node(data)
            temp.next.next=self.head
        print("Data inserted Successfull")
        print("Insert at end operations completed successfully")

    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next==self.head:
                self.head=None
            else:
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                del_node=self.head
                self.head=self.head.next
                temp.next=self.head
                print(del_node.data,"is deleted successfully")
                del(del_node)
        print("Delete at Begin operation is completed successfully")
    #complete it fully
    def delete_at_position(self,pos):
        if self.head is None:
            print("List is Empty")
        else:
            count=0
            temp=self.head
            if self.head.next==self.head:
                self.head=None
                print(temp.data,"is deleted successfully")
                del(temp)
            elif pos==0:
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                del_node=self.head
                temp.next=self.head.next
                self.head=self.head.next
                print(del_node.data,"is deleted successfully")
                del(del_node)
            else:
                prev=None
                while (pos)!=count and temp is not None:
                    prev=temp
                    temp=temp.next
                    count+=1
                if temp==None:
                    print("Index out of range")
                else:
                    prev.next=temp.next
                    print(temp.data,"is deleted successfully")
                    del(temp)
            print('Delete at Position operation completed successfully')
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            prev=None
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at End operation is completed successfully")

    def search(self,num):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            count=0
            while temp and temp.data!=num:
                temp=temp.next
                count+=1
            if temp is not None:
                print(num,"Found at index: ",count)
            else:
                print(num,"Not Present in the List")
        print("Search operation completed successfully")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head.next
            print(self.head.data,end=' ')
            if self.head.next!=self.head:
                print('->',end=' ')
            while temp!=self.head:
                print(temp.data,end=' ')
                if temp.next!=self.head:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")
    
print("""1.Insert at Begin\n2.Insert at Index\n3.Insert at End
4.Delete at Begin\n5.Delete at Position\n6.Delete at end\n7.Search\n8.Display\n9.Exit\n""")
o=CSL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter data to insert at begin:"))
        o.insert_at_begin(data)
    elif ch==2:
        index=int(input("Enter index position:"))
        data=int(input("Enter Data to insert at given index:"))
        o.insert_at_index(data,index)
    elif ch==3:
        data=int(input("Enter Data to insert at end:"))
        o.insert_at_end(data)
    elif ch==4:
        o.delete_at_begin()
    elif ch==5:
        pos=int(input("Enter Position to delete:"))
        o.delete_at_position(pos)
    elif ch==6:
        o.delete_at_end()
    elif ch==7:
        num=int(input("Enter Number to Search:"))
        o.search(num)
    elif ch==8:
        o.display()
    elif ch==9:
        print('\n\t********Your Exited********\n\t\t**THE END**\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")