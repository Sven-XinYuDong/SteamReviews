import unittest
from UnitTest_DataExtract import TestExtract
from Unitest_APICall_RA import *

def Steam_TestSuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    suite.addTest(unittest.makeSuite(TestExtract))
    suite.addTest(unittest.makeSuite(TestAPICall))
    suite.addTest(unittest.makeSuite(TestReview))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
Steam_TestSuite()
