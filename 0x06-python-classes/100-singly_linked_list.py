#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value and type(value) != Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value, None)
        if (self.__head):
            aux_node = self.__head
            while (aux_node):
                if (new_node.data < aux_node.data):
                    new_node.next_node = aux_node
                    aux_node = new_node
                else:
                    if (aux_node.next_node):
                        aux_node = aux_node.next_node
                    else:
                        aux_node.next_node = new_node
        else:
            self.__head = new_node


    def __str__(self):
        str_list = ""
        aux_node = self.__head
        while (aux_node):
            str_list += str(aux_node.data) + "\n"
            aux_node = aux_node.next_node
        return (str_list)
