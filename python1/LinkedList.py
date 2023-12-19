class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.next is not None:
                currentnode = currentnode.next
            currentnode.next = newnode

    def nodebiginig(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def delete_values(self,value):
        if self.head is None:
            print("Linked List Empty")
            return
        if self.head.data == value:
            self.head = self.head.next
        else:
            currentnode = self.head
            while currentnode.next is not None:
                if currentnode.next.data == value:
                    currentnode.next = currentnode.next.next
                    return
                currentnode = currentnode.next


    def display(self):
        if self.head is None:
            print("Linked list Empty")
        else:
            currentnode = self.head
            while currentnode is not None:
                print(currentnode.data, end=" ")
                currentnode = currentnode.next


linkedlist = LinkedList()
linkedlist.addnode(2)

linkedlist.display()