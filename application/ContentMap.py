from application.AbstractMap import AbstractMap
from application.Tree import Tree


class ContentMap(AbstractMap):
    """
        Python does not have a HashMap like Java or Kotlin
        Instead of it, it has a dict that works the same way and is easily see as a json.

        @self.__dictionary - save the different values for different keys
        @self.__allValues - save the value for all elements when set
        @self.__treeExistent - save all the keys elements, this is needed to check if an element exists
    """
    def __init__(self):
        self.__dictionary = dict()
        self.__allValues = None
        self.__treeExistent = None
        self.__dictionaryAll = dict()

    def setTree(self, tree):
        self.__treeExistent = tree

    def getTreeWay(self, key):
        """
        To solve the problem to check if a key exists or not on the group,
        I create a binary tree to save all the existent keys on the hash.
        This add to get a complexity of O(n log n) in average cases, worst case O(n)
        :param key: searched element
        :return: string info if the searched element does not exists, value if exists
        """
        try:
            result = self.__dictionary[key]
        except Exception:
            if self.__treeExistent.search(key) is not None:
                result = self.__allValues
            else:
                result = "The element does not exist!"
        return result

    def getHashWay(self, key):
        """
        If we use two dicts would be easy to check if the key exists, we can do it on O(1)
        because dicts consults like hash, and its always O(1) because it check directly on hash tables.
        This case, instead of search on a tree, it checks if exists on the dictionary that saves all values with
        None to not occupy more space than necessary, we just need space to save the keys.
        :param key: searched element
        :return: string info if the searched element does not exists, value if exists
        """
        try:
            result = self.__dictionary[key]
        except Exception:
            try:
                self.__dictionaryAll[key]
                result = self.__allValues
            except Exception:
                result = "The element does not exist!"
        return result

    def set(self, key, value):
        """
        This set serves for the tow ways of get, we set a value on the dictionary
        also set the value on the tree and on the dictionary to save all
        that's just for test when we choose one way we just delete the one that would be unused
        :param key: key to set specific element
        :param value: value to key reference
        :return: nothing
        """
        self.__dictionary[key] = value
        if self.__treeExistent is not None:
            self.__treeExistent.insert(key)
        self.__dictionaryAll[key] = None

    def setAll(self, value):
        """
        Here is the real trick, when we set a value for all, we just need to reset the dictionary
        that saves the different ones
        :param value: value to set for all
        :return: nothing
        """
        self.__dictionary = dict()
        self.__allValues = value
