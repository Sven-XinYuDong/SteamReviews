import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

import unittest
import pandas as pd
import requests

from SteamFunctions.SteamDataFrameConverter import friendlist_to_dataframe, chart_dataframe
from SteamFunctions.SteamDataExtraction import extract_data


class TestDataFrameConvert(unittest.TestCase):
    def test_friendlist_to_dataframe(self):
        extracted = extract_data(76561197996661065)
        self.assertEqual(type(friendlist_to_dataframe(extracted)), pd.core.frame.DataFrame)
        self.assertEqual("matt" in friendlist_to_dataframe(extracted).values, True)
    def test_chart_dataframe(self):
        dataframe = friendlist_to_dataframe(extract_data(76561197996661065))
        self.assertEqual(chart_dataframe(dataframe)["Text"][0], "Total number of games owned")
        self.assertEqual("TotalNumGames" in chart_dataframe(dataframe)["variable"].values, True)
        self.assertEqual(chart_dataframe(dataframe).columns.tolist(), ['Name', 'ProfilePicture', 'GameList', 'variable', 'value', 'Text'])
