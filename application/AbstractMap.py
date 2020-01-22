class AbstractMap(object):
    """ This is an abstract class! """
    """ Like python does not have interfaces, we define an abstract class. """
    """ Python does not have interfaces because it accepts multiples extends. """
    def getTreeWay(self, key):
        raise NotImplemented("Implement this method!")

    def getHashWay(self, key):
        raise NotImplemented("Implement this method!")

    def set(self, key, value):
        raise NotImplemented("Implement this method!")

    def setAll(self, value):
        raise NotImplemented("Implement this method!")