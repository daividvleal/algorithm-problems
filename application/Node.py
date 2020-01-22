class Node:
    def __init__(self, name: int, children: [], parent=None):
        self.__name = name
        self.__children = children
        self.__parent = parent

    def getParent(self):
        return self.__parent

    def setParent(self, node):
        self.__parent = node

    def left(self):
        return self.__children[0]

    def right(self):
        return self.__children[1]

    def value(self):
        return self.__name

    def name(self):
        return str(self.__name)

    def __str__(self):
        result = "Searched element: " + self.name() + "\n"
        if self.left() is not None:
            result += "Left node: " + str(self.left().name()) + "\n"
        if self.right() is not None:
            result += "Right node: " + str(self.right().name()) + "\n"
        return result

    def setRight(self, node):
        self.__children[1] = node

    def setLeft(self, node):
        self.__children[0] = node
