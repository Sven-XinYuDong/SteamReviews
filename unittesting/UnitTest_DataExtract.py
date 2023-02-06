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

from SteamFunctions.SteamDataExtraction import get_friend_id, get_friend_name, get_game_library, get_game_prices, extract_data
class TestExtract(unittest.TestCase):
	def test_getFriend(self):
		self.assertEqual(type(get_friend_id(76561197996661065)), list)
		self.assertNotEqual(get_friend_id(76561197996661065), None)
		self.assertEqual(type(int(get_friend_id(76561197996661065)[0])), int)
	def test_getFriendName(self):
		friendId = get_friend_id(76561197996661065)
		friendName = get_friend_name(friendId)
		self.assertEqual(type(friendName), dict)
		self.assertEqual(friendName["matt"][1][-3:], "jpg")
		self.assertNotEqual(friendName["matt"], None)
	def test_getLibrary(self):
		friendNameList = get_friend_name(get_friend_id(76561197996661065))
		friendNameGameLibrary = get_game_library(friendNameList)
		self.assertNotEqual(friendNameGameLibrary["matt"][2], None)
		self.assertEqual(type(friendNameGameLibrary["matt"]), list)
		self.assertEqual(type(friendNameGameLibrary["matt"][2][0]), dict)
		self.assertEqual(friendNameGameLibrary["matt"][2][0]["name"], "Counter-Strike: Source")
	def test_getPrice(self):
		friendNameGameList = get_game_library(get_friend_name(get_friend_id(76561197996661065)))
		friendNameGamePriceList = get_game_prices(friendNameGameList)
		self.assertNotEqual(friendNameGamePriceList["matt"][2][0]["price"], None)
		self.assertEqual(friendNameGamePriceList["matt"][2][0]["price"], 12.99)
	def test_extractData(self):
		extractList = extract_data(76561197996661065)
		self.assertEqual(len(extractList), len(get_game_prices(get_game_library(get_friend_name(get_friend_id(76561197996661065))))))
		self.assertNotEqual(extractList, None)
