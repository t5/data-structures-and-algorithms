import unittest

"""Implements a singly-linked list"""

class Node:
    """A single node in a singly-linked list"""

    def __init__(self, value):
        self.next_node = None
        self.value = value

    def getNext(self):
        return self.next_node

    def getValue(self):
        return self.value

    def setNext(self, next_node):
        self.next_node = next_node

    def setValue(self, value):
        self.value = value

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insert(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(newNode)

    def remove(self, item):
        temp = self.head
        if self.head.getValue() == item:
            self.head = self.head.getNext()
            return

        prev = None
        while temp.getNext() != None:
            if temp.getValue() == item:
                # found
                prev.setNext(temp.getNext())
            prev = temp
            temp = temp.getNext()
        if temp.getValue() == item:
            prev.setNext(None)

    def traverse(self):
        if self.isEmpty():
            return
        temp = self.head
        while temp.getNext() != None:
            print(temp.getValue())
            temp = temp.getNext()
        print(temp.getValue())

    def search(self, value):
        temp = self.head
        while temp.getNext() != None:
            if temp.getValue() == value:
                return temp
            temp = temp.getNext()
        if temp.getValue() == value:
            return temp
        return -1

    def size(self):
        count = 0
        if self.isEmpty():
            return 0
        temp = self.head
        while temp.getNext() != None:
            temp = temp.getNext()
            count += 1
        count += 1
        return count

class TestLinkedList(unittest.TestCase):
    """Tests for LinkedList"""

    def test_empty(self):
        trial = LinkedList()
        self.assertTrue(trial.isEmpty())
        trial.insert('hello')
        self.assertFalse(trial.isEmpty())

    def test_size(self):
        trial = LinkedList()
        self.assertEqual(trial.size(), 0)
        trial.insert('hello')
        self.assertEqual(trial.size(), 1)

if __name__ == "__main__":
    unittest.main()
