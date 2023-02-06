import unittest
from UnitTest_DataExtract import TestExtract

def Steam_TestSuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestExtract))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
Steam_TestSuite()
