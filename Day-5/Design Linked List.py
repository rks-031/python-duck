class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def get_size(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        return size

    def get(self, index: int) -> int:
        size = self.get_size()
        if index >= size:
            return -1
        i = 0
        temp = self.head
        while temp:
            if i == index:
                return temp.val
            i += 1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = self.Node(val)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        size = self.get_size()
        if index > size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == size:
            self.addAtTail(val)
            return
        newNode = self.Node(val)
        i = 0
        temp = self.head
        while temp:
            if i == index - 1:
                newNode.next = temp.next
                temp.next = newNode
                return
            i += 1
            temp = temp.next

    def deleteAtIndex(self, index: int) -> None:
        size = self.get_size()
        if index >= size:
            return
        if index == 0:
            self.head = self.head.next
            return
        i = 0
        temp = self.head
        while temp:
            if i == index - 1 and temp.next:
                temp.next = temp.next.next
                return
            i += 1
            temp = temp.next
