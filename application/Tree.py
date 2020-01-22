from application.Node import Node


class Tree:
    def __init__(self, node: Node = None):
        self.__node_root = node

    def getRoot(self):
        return self.__node_root

    def setRoot(self, node):
        self.__node_root = node

    def inOrderTraversal(self, node=None):
        if node is not None:
            self.inOrderTraversal(node.left())
            print(node.name())
            self.inOrderTraversal(node.right())

    def preOrderTraversal(self, node=None):
        if node is not None:
            print(node.name())
            self.preOrderTraversal(node.left())
            self.preOrderTraversal(node.right())

    def postOrderTraversal(self, node=None):
        if node is not None:
            self.postOrderTraversal(node.left())
            self.postOrderTraversal(node.right())
            print(node.name())

    def search(self, searched, node=None, searchOnTree=True):
        if node is not None:
            if node.value() == searched:
                return node
            if node.value() > searched:
                return self.search(searched, node.left(), False)
            elif node.value() < searched:
                return self.search(searched, node.right(), False)
        elif searchOnTree:
            return self.search(searched, self.getRoot(), False)
        else:
            return None

    def insert(self, value, insertOnTree=True, node=None):
        if insertOnTree and self.getRoot() is None:
            self.setRoot(Node(value, [None, None], None))
        elif insertOnTree and self.getRoot() is not None:
            self.insert(value, False, self.getRoot())
        elif value > node.value() and node.right() is None:
            node.setRight(Node(value, [None, None], node))
        elif value > node.value() and node.right() is not None:
            self.insert(value, False, node.right())
        elif value < node.value() and node.left() is None:
            node.setLeft(Node(value, [None, None], node))
        elif value < node.value() and node.left() is not None:
            self.insert(value, False, node.left())

    def isBST(self, min=None, max=None, node=None, verifyThis=True):
        if node is None and verifyThis:
            if self.getRoot() is None:
                return True
            else:
                return self.isBST(self.findMin().value(), self.findMax().value(), self.getRoot(), False)
        elif node is None:
            return True
        elif node.value() < min or node.value() > max:
            return False
        else:
            return self.isBST(min, node.value() - 1, node.left(), False) \
                   and \
                   self.isBST(node.value() + 1, max, node.right(), False)

    def findMin(self, node=None):
        if self.getRoot() is None:
            return "The tree is empty"
        elif node is None:
            return self.findMin(self.getRoot())
        elif node.left() is not None:
            return self.findMin(node.left())
        else:
            return node

    def findMax(self, node=None):
        if self.getRoot() is None:
            return "The tree is empty"
        elif node is None:
            return self.findMax(self.getRoot())
        elif node.right() is not None:
            return self.findMax(node.right())
        else:
            return node

    def __str__(self):
        self.print()
        return ""

    def print(self, node=None, printThis=True):
        if node is None and printThis:
            self.print(self.getRoot(), False)
        else:
            if node is None:
                return ""
            else:
                self.print(node.left(), False)
                print(node)
                self.print(node.right(), False)

    def __build(self, sortedArray, parent=None):
        if not sortedArray:
            return None
        else:
            middle = int(len(sortedArray) / 2)
            node = Node(sortedArray[middle], [None, None], parent)
            node.setLeft(self.__build(sortedArray[:middle], node))
            node.setRight(self.__build(sortedArray[middle + 1:], node))
            return node

    def buildTree(self, sortedArray):
        self.setRoot(self.__build(sortedArray))

    def replaceNodeParent(self, node=None):
        if node is None:
            return
        elif node.parent is not None:
            if node == node.parent.left():
                node.getParent().setLeft(node)
            else:
                node.getParent().setRight(node)
        if node is not None:
            node.setParent(node.getParent())
