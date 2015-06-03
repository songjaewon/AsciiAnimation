__author__ = 'cimple'

class TestClassB():
    """
    This class is initial class of docuModuleB.
    """
    def __init__(self, argA, argB, argC):
        """
        Initial function for TestClassB
        :param argA: input argument A
        :param argB: input argument B
        :param argC: input argument C
        :return: None
        """
        self._argA = argA
        self._argB = argB
        self._argC = argC
        self._argumentList = []
        self.initCrateList()


    def initCrateList(self):
        """
        Initialize function to create argument list
        :return:None
        """
        self._argumentList.append([self._argA, self._argB, self._argC])

