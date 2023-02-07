import requests

def get_friend_id(steamId):
    friendIds = []
    try:
        friendlist = requests.get("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=3D41F12368AF3E305A8233ABFB965CA2&relationship=friend&steamid=" + str(steamId)).json()

        friendIds.append(str(steamId))
        for friend in friendlist["friendslist"]["friends"]:
            friendIds.append(friend["steamid"])
    except:
        print("Error occurred in extracting friend list")

    return friendIds


def get_friend_name(friendIds):
    friendSearchQuery = ""
    for i in friendIds:
        friendSearchQuery += i + ","
    try:
        friendName = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=3D41F12368AF3E305A8233ABFB965CA2&steamids=" + friendSearchQuery[:-1]).json()
        friendNameList = {}
        for friendName in friendName["response"]["players"]:
            friendNameList[friendName["personaname"]] = []
            friendNameList[friendName["personaname"]].append(friendName["steamid"])
            friendNameList[friendName["personaname"]].append(friendName["avatar"])
    except:
        print("Error occurred in extracting friend names")
    return friendNameList

def get_game_library(friendNameList):
    for friend in friendNameList:
        try:
            gameLibrary = requests.get("https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=3D41F12368AF3E305A8233ABFB965CA2&include_appinfo=1&format=json&steamid="
                                       + friendNameList[friend][0]).json()["response"]["games"]
            friendNameList[friend].append(gameLibrary)
        except:
            print("Could not load game library for", friend)
    for friend in list(friendNameList):
        if len(friendNameList[friend]) == 2:
            del(friendNameList[friend])
    return friendNameList



def get_game_prices(friendNameList):
    try:
        appIdList = []
        for friend in friendNameList:
            for game in friendNameList[friend][2]:
                appIdList.append(game["appid"])
        appString = ""
        for app in appIdList:
            appString = appString + str(app) + ","
        prices = requests.get("https://store.steampowered.com/api/appdetails?appids=" + appString + "&filters=price_overview").json()
        for friend in friendNameList:
            for game in friendNameList[friend][2]:
                try:
                    if prices[str(game["appid"])]["success"]:
                        if prices[str(game["appid"])]["data"] != []:
                            game["price"] = float(prices[str(game["appid"])]["data"]["price_overview"]["final_formatted"][5:])
                except:
                    pass
    except:
        pass
    return friendNameList

def extract_data(steamId):
    try:
        friendId = get_friend_id(steamId)
        idAndName = get_friend_name(friendId)
        idNameLibrary = get_game_library(idAndName)
        prices = get_game_prices(idNameLibrary)
    except:
        print("Error occurred in loading data")
    return prices
