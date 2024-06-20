#Binary Search Tree
#Node Creation
class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None

#Insert the Node into the Tree
def insert(root,key):
    if root is None:
        return Node(key)
    if root.key==key:
        print("Duplicates are not allowed")
    elif root.key < key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root

#Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

#Deleting the Node from the Tree
def delete(root,data):
    #Traversing the Tree till the Node found
    if root is None:
        print("Not Found")
        print("Element is not found")
        return
    elif data < root.key:
        print(root.key,'->',end=' ')
        root.left=delete(root.left,data)
    elif data > root.key:
        print(root.key,'->',end=' ')
        root.right=delete(root.right,data)
    else:
        print(root.key)
        if root.left is None:
            #Leaf Node
            if root.right is None:
                print("Node with no child")
            #Node with Right Child
            else:
                print("Node with one child")
            temp=root.right
            print(temp)
            return temp
        elif root.right is None:
            #Leaf Node
            if root.left is None:
                print("Node with no child")
            #Node with Left Child
            else:
                print("Node with one child")
            temp=root.left
            return temp
        #Node with 2 Children
        else:
            print("Node with 2 children")
            temp=root.right
            prev=None
            while temp.left:
                prev=temp
                temp=temp.left
            if prev is not None:
                prev.left=temp.right
                temp=root.right
            temp.left=root.left
            return temp
    return root
    #print("Delete operation completed successfully")

#Searching for the Element in Tree
def search(root,key):
    if root is None:
        print("elemnt not found")
    if root.key==key:
        print("element found")
        return
    elif root.key < key:
        search(root.right,key)
    else:
        search(root.left,key)

#Code Starts from here
root=None
while True:
    print("1.Insert\n2.Inorder Traversal\n3.Delete\n4.Search\n5.Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        data=int(input("Enter Data to insert:"))
        root=insert(root,data)
    elif ch==2:
        print("Inoder Traversal:- ",end=' ')
        inorder(root)
        print()
    elif ch==3:
        key=int(input("Enter data to delete:"))
        delete(root,data)
    elif ch==4:
        key=int(input("Enter data to search:"))
        search(root,key)
    elif ch==5:
        print("\t**THE END**")
        break
    else:
        print("Invalid Choice")