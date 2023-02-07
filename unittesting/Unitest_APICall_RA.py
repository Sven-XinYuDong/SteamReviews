import sys
import os
import re
packagepath = os.path.abspath(__file__)
packagepath = re.sub(r'\/[^\/]*\/{1}[^\/]*(\.).*', '', packagepath)
if not packagepath in sys.path:
	sys.path.append(packagepath)

import unittest
import pandas as pd
import random as rand
import requests
import json


import APICall
class TestAPICall(unittest.TestCase):
	key = APICall.set_key('3D41F12368AF3E305A8233ABFB965CA2')

	def test_get_n_reviews(self):
		self.assertEqual(type(APICall.get_n_reviews(413150,1)),pd.core.frame.DataFrame)

	def test_get_friend_list(self):
		self.assertEqual(type(APICall.get_friend_list('76561197996661065')),pd.core.frame.DataFrame)

	def test_get_games_owned(self):
		self.assertEqual(type(APICall.get_games_owned('76561197996661065')),pd.core.frame.DataFrame)

	def test_get_game_genres(self):
		self.assertEqual(type(APICall.get_game_genres('105600')),pd.core.frame.DataFrame)

	def test_compare_genres_preference(self):
		self.assertEqual(type(APICall.compare_genres_preference(['76561198025087893','76561198036542086'])),pd.core.frame.DataFrame)





import Reviews_Analysis
class TestReview(unittest.TestCase):
	key = APICall.set_key('3D41F12368AF3E305A8233ABFB965CA2')
	review_df = APICall.get_n_reviews(413150,1)

	def test_review_sentiments(self):
		sentiments_df = Reviews_Analysis.review_sentiments(review_df)
		self.assertEqual(type(sentiments_df),pd.core.frame.DataFrame)

	def test_reveiew_cloud(self):
		self.assertEqual(type(Reviews_Analysis.reveiew_cloud(['76561198025087893','76561198036542086'])),str)
