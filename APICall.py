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

### Dependencies
import requests
import pandas as pd
import json
import re

### Run this code block to change how many reviews we want to get
def get_reviews(appid, params={'json':1}):
    '''
    Get game reveiw data from steampowered API in JSON format
    '''

    url = 'https://store.steampowered.com/appreviews/'
    response = requests.get(url=url+str(appid), params=params, headers={'User-Agent': 'Mozilla/5.0'})
    return response.json()


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


def review_cleaning(df):
    '''
    Clean the review to be lower cased and without punctuation
    '''

    rt = lambda x: re.sub("[^a-zA-Z]",' ',str(x))
    df['review'] = df['review'].map(rt) # remove punctuation and numbers
    df['review'] = df['review'].str.lower() #all lower cased
    return df
