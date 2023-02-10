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
import altair as alt

from SteamFunctions.SteamDataFrameConverter import friendlist_to_dataframe, chart_dataframe
from SteamFunctions.SteamDataExtraction import extract_data
from SteamFunctions.SteamChartCreator import compare_chart, development_dashboard

class TestChart(unittest.TestCase):
    def test_compare_chart(self):
        data = extract_data(76561197996661065)
        chart_data = chart_dataframe(friendlist_to_dataframe(data))
        self.assertEqual(type(compare_chart(chart_data)), alt.vegalite.v4.api.LayerChart)
        self.assertNotEqual(compare_chart(chart_data), None)
    def test_development_dashboard(self):
        data = extract_data(76561197996661065)
        chart_data = chart_dataframe(friendlist_to_dataframe(data))
        self.assertEqual(type(development_dashboard(chart_data)), alt.vegalite.v4.api.HConcatChart)
        self.assertNotEqual(development_dashboard(chart_data), None)
