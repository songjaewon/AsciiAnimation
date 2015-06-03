__author__ = 'cimple'

"""
This Python code is docuModuleA
"""

def public_ftn_docuModuleA(argA, argB):
    """
    This function is public function of docuModuleA

    Args:
       argA (int): Input argument A
       argB (int): Input argument B

    Returns:
       int. argument A + argument B
    """
    return argA+argB

class TestClassA():
    """
    This test class A is for the initial class of docuModule A.
    """
    def __init__(self, argA, argB=0.0):
        """
        Class initializer.
        :param argA: argumant A.
        :param argB: argument B. Initial value is 0.
        :return:
        """
        self._argA = argA
        self._argB = argB

    def getArgumentA(self):
        """
        This function could get the argument A
        :return:
        """
        return self._argA

    def calculateArguments(self, argC, argD):
        """
        This function calculate summation of class argument A,B and input argument C,D
        :param argC: Additional arguments for class argument A.
        :param argD: Additional arguments for class argument B.
        :return: Summation of all arguments, A,B,C, and D.
        """
        print self._argA+argC
        print self._argB+argD
        return self._argA+argC+self._argB+argD
