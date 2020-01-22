from application.Tree import Tree
from application.Node import Node
from application.ContentMap import ContentMap
import time


def main():
    contentMap = ContentMap()
    """ Fill the hash with some different values! """
    ammount = 9999999
    array_elements_keys = [str(n) for n in range(-ammount, ammount)]
    array_elements = [n for n in range(-ammount, ammount)]
    for i in range(0, len(array_elements_keys) - 1):
        contentMap.set(array_elements_keys[i], array_elements[i])
    """ build balanced search tree - BST """
    tree = Tree()
    tree.buildTree(array_elements_keys)
    contentMap.setTree(tree)

    print(contentMap.getHashWay("0"))
    print(contentMap.getHashWay("142154"))
    print(contentMap.getHashWay("14215432434"))
    contentMap.setAll(50)
    contentMap.set(str(len(array_elements_keys) - 1), len(array_elements_keys) - 1)
    print(contentMap.getHashWay(str(len(array_elements_keys) - 1)))
    print(contentMap.getHashWay("0"))
    print(contentMap.getHashWay("142154"))
    print(contentMap.getHashWay("14215432434"))

    a = int(round(time.time() * 1000000000))
    contentMap.getHashWay("9999998")
    b = int(round(time.time() * 1000000000))
    print("Hash way Takes: " + str(b - a) + " nanoseconds.")

    a = int(round(time.time() * 1000000000))
    contentMap.getTreeWay("9999998")
    b = int(round(time.time() * 1000000000))
    print("BST way Takes: " + str(b - a) + " nanoseconds.")


if __name__ == '__main__':
    main()

"""
output:

0
142154
The element does not exist!
19999997
50
50
The element does not exist!
Hash way Takes: 48128 nanoseconds.
BST way Takes: 56064 nanoseconds.

By increase to infinity Hash way will tend to take the same time(time to see the key on the hash table)
 because its O(1).
and BST way will grow logarithmically because it's O(n log n) / worst case O(n)
"""
