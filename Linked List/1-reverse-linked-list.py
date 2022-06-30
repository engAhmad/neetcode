
class Node:
    # Constructor to initialize the node object
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to Append new node at the end.
    def append(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # Function to Append new nodes as array.
    def insertMulti(self, list):
        for item in list:
            self.append(item)

    # printing the data in the linked list
    def printLinkedList(self):
        current = self.head
        items = []
        while(current):
            items.append(current.data)
            current = current.next
        print(items)

    # Function to reverse the linked list
    # 1 -save current.next in temp 
    # 2 - current.next = prev  -> become <-
    # 3 previous = current
    def reverseList(self):
        previous = None
        current = self.head
        while (current is not None):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous
    def reverseListRec(self,head):
       # base case 
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRec(head.next)
            head.next.next = head
        head.next = None
        return newHead
# Driver code
list = LinkedList()
list.insertMulti([1, 2, 3, 4, 5])
#list.printLinkedList()
list.reverseListRec()
list.printLinkedList()
