#!/usr/bin/python3
"""Node of a Singly Linked List.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node.
"""


class Node:
    """Node class. """

    def __init__(self, data, next_node=None):
        """initializes node data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the Node data."""
        return self.__data

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets the data into a node."""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.
        Args:
            value (Node, optional): Node or None
        Raises:
            TypeError: If `value` is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class."""

    def __init__(self):
        """initializes the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert - inserts node in a sorted linked list
        Args:
            value (int): data of new node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            curr = self.__head
            while curr.next_node:
                if new.data >= curr.data and new.data <= curr.next_node.data:
                    new.next_node = curr.next_node
                    curr.next_node = new
                    break
                elif new.data < curr.data:
                    new.next_node = curr
                    self.__head = new
                    break
                curr = curr.next_node
            if new.data >= curr.data:
                curr.next_node = new
            else:
                new.next_node = curr
                self.__head = new

    def __str__(self):
        """string representation of singly linked list
        Returns:
            my_str: new-line separated list string
        """
        curr = self.__head
        my_str = ''
        if curr is None:
            my_str = ''
        elif curr.next_node is None:
            my_str += str(curr.data)
        else:
            while curr.next_node:
                my_str += str(curr.data) + '\n'
                curr = curr.next_node
            my_str += str(curr.data)
        return my_str


if __name__ == '__main__':
    sll = SinglyLinkedList()

    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
