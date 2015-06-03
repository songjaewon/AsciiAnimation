__author__ = 'cimple'

"""
This Python code is docuModuleB
"""

def public_ftn_docuModuleB(argA, argB):
    """
    This function is public function of docuModuleB
    :param argA: argument A
    :param argB: argument B
    :return: return value
    """
    return argA-argB

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

