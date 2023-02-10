# !/usr/bin/python
#
# Copyright (C) 2023 Xinyu Dong, Mattew Yau.
# You may obtain a copy of the License at
#
# https://github.com/Sven-XinYuDong/SteamSMART/blob/main/LICENSE.md
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#### Dependencies
import requests
import pandas as pd
import json
import re
import numpy as np

#### Get game reviews from Steam
def get_reviews(appid, params={'json':1}):
    '''
    Get game reveiw data from steampowered API in JSON format
    '''
    try:
        url = 'https://store.steampowered.com/appreviews/'
        response = requests.get(url=url+str(appid), params=params, headers={'User-Agent': 'Mozilla/5.0'})
        return response.json()

    except Exception as ex:
        print('connection failed, check if the appid is valid')


def get_n_reviews(appid, n = 40): ## Change this line to change number of reviews we want to obtain.
    '''
    Get the specified number of game comments in a Pandas DataFrame

    Parameters:
        appid - this is the ID for the game in Steam Store
        n - the multiple number of each 100 review entries

    Returns:
        return the reviews details in a Pandas DataFrame
    '''

    reviews = pd.DataFrame()
    cursor = "*"
    params = {
        "json" : 1,
        "num_per_page": 100,
        "review_type": "all"
    }
    try:
        while n > 0:
            params["cursor"] = cursor.encode()
            n -= 1

            response = get_reviews(appid, params)
            cursor = response["cursor"]

            d = response
            d.pop('success')
            d.pop('query_summary')
            df = pd.DataFrame(d['reviews'])
            reviews = pd.concat([reviews,df])
        return reviews

    except Exception as ex:
        print('n out of bound')


def review_cleaning(df):
    '''
    Clean the review to be lower cased and without punctuation
    '''

    rt = lambda x: re.sub("[^a-zA-Z]",' ',str(x))
    df['review'] = df['review'].map(rt) # remove punctuation and numbers
    df['review'] = df['review'].str.lower() #all lower cased
    return df


def set_key(user_key):
    '''
    global key for Steam API
    '''
    global key
    key = user_key


##### get_friend_list(steamid)
def get_friend_list(steam_id):
    '''
    Get the friend list given a steam_id,return a DataFrame of friends's steamid

    Parameters:
        steam_id - the Steam ID to look up

    Returns:
        A DataFrame with friends'id, relationship and being friends since when
    '''

    #Formulate url

    url_friends_prefix = " http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="
    url_tail = '&relationship=friend'
    try:
        url = url_friends_prefix+key+'&steamid='+steam_id+url_tail

    except Exception as ex:
        print('key not found, use set_key(user_key) to set up Steam API key ')

    try:
        response = requests.get(url)  #Get response

        #Return pandas DataFrame
        friends = json.loads(response.text)
        friends = pd.DataFrame(friends['friendslist']['friends'])
        return friends

    except Exception as ex:
        print('steamid not valid')



#### get_games_owned(steam_id)
def get_games_owned(steam_id):
    '''
    Get the games details owned by given Steam ID

    Parameters:
        steam_id - the id to to specify player

    Returns:
        A DataFrame with appid, game name, playtime and other related details of owned games

    '''
    #Formulate url
    key = "3D41F12368AF3E305A8233ABFB965CA2"
    url_owneGames_prefix = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    url_ownGames_tail = "&include_appinfo=1&format=json"
    url = url_owneGames_prefix+key+'&steamid='+steam_id+url_ownGames_tail

    response = requests.get(url)  #Get response

    #Return pandas DataFrame
    games = json.loads(response.text)
    games = pd.DataFrame(games['response']['games'])
    return games


#### get_game_genre(app_id)
def get_game_genres(app_id):
    '''
    Get the genre infomation of an given app

    Parameters:
        app_id: the id of games in Steam Store

    Returns:
        A list of genres description for the App
    '''
    #Formulate url
    url_gamedetail_prefix = "https://store.steampowered.com/api/appdetails/?appids="
    url_gamedetail_tail = "&cc=EE&l=english&v=1 HTTP/1.1" "-" "Valve/Steam HTTP Client 1.0 (tenfoot)"
    url = url_gamedetail_prefix+app_id+url_gamedetail_tail

    response = requests.get(url)  #Get response

    #Return a list of genres tags
    try:
        detail = requests.get(url).json()[app_id]["data"]
        detail = pd.DataFrame(detail['genres'])
        genres = list(detail.description)
        return genres

    except:
        return ['NA']


#### compare_genres_preference(steam_id_list)
def compare_genres_preference(steam_id_list):
    '''
    Provide a summary table of the genres of games owned by user in a list of Steam IDs.

    Parameters:
        steam_id_list - a list of Steam IDs

    Returns:
        A Dataframe with Steam IDs and correspondent genres belonging to games they own.
    '''

    id_genres_df = pd.DataFrame()

    try:
        for steam_id in steam_id_list:
            games_owned = get_games_owned(steam_id)
            #Add genres infomation to game DataFrame
            games_owned['genres'] = games_owned['appid'].apply(str).apply(get_game_genres)

            #unnest genres into long Dataframe for Viz
            long_tags = []
            for tag in games_owned['genres']:
                long_tags += tag
            d = {'steamid': list(np.repeat(steam_id,len(long_tags))),
                 'genres':long_tags }
            df = pd.DataFrame(d)
            id_genres_df = pd.concat([id_genres_df,df])

        return id_genres_df

    except Exception as ex:
        print(ex)
