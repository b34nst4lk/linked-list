from node import Node

class SinglyLinkedList:
    def __init__(self, *values):
        self.head = Node(values[0])

        node = self.head
        for value in values:
            node.next = Node(value) 
            node = node.next


    def __getitem__(self, i):
        if type(i) is not int:
            raise KeyError("index should be int")
        
        node = self.head
        for _ in range(i):
            if node.next is None:
                raise IndexError
            node = node.next

        return node

    def __setitem__(self, i, value):
        self[i].value = value
        pass

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def extend(self, value):
        node = self.head
        while (node.next is not None):
            node = node.next
        
        node.next = Node(value)

    def insert(self, i, value):
        newNode = Node(value)
        if i == 0:
            newNode.next = self.head
            self.head = newNode

        else:
            nodeA = self[i - 1]
            nodeA.next = newNode
            
            nodeB = self[i]
            newNode.next = nodeB