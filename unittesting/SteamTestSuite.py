import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

from unittesting.UnitTest_DataExtract import TestExtract
from unittesting.Unitest_APICall_RA import *
from unittesting.UnitTest_DataframeConvert import TestDataFrameConvert
from unittesting.UnitTest_ChartCreator import TestChart


def Steam_TestSuite():
	suite = unittest.TestSuite()
	result = unittest.TestResult()
	suite.addTest(unittest.makeSuite(TestExtract))
	suite.addTest(unittest.makeSuite(TestAPICall))
	suite.addTest(unittest.makeSuite(TestReview))
	suite.addTest(unittest.makeSuite(TestDataFrameConvert))
	suite.addTest(unittest.makeSuite(TestChart))
	runner = unittest.TextTestRunner()
	print(runner.run(suite))
Steam_TestSuite()
