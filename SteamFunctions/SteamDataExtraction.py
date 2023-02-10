import requests

def get_friend_id(steamId):
    '''
    This function obtains the friendlist (in the form of friend steamIDs) of a
    person.

    Parameters:
        steamId: int
            A 17 digit steam ID of your account, which could be found by
            navigating to your profile (in steamcommunity.com, navigate to top right
            corner, select view profile). After viewing your profile, in the url,
            your steamID could be found by the last 17 digits of your url.
            e.g. https://steamcommunity.com/profiles/76561197996661065/,
            76561197996661065 is the steam ID.

    Returns:
        friendIds: list
            A list of you and your friends steam IDs.
    '''
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
    '''
    This function obtains the account (profile) names and avatar pictures
    tied to a person's steamID.

    Parameters:
        friendIds: list
            This is a list containing a number of steam IDs you want
            to obtain the names for. Example: [76561197996661065, ...]

    Returns:
        friendNameList: dictionary
            A dictionary, with profile name as the key, and for values, a list
            (containing steamIDs and profile picture)
    '''
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
    '''
    This function obtains the game libraries tied to a person's account.

    Parameters:
        friendNameList: list
            This is a dictionary containing person's profile names
            as key, and as values, a list (containing steamID and profile pictures)

    Returns:
        friendNameList: dict
            A dictionary, with person's profile names as key, and as values,
            a list (containing steamID, profile picture, and game library)
    '''
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
    '''
    This function obtains the game prices (full price) for game libraries within people's
    accounts.

    Please note that the current function does not allow searching for more than 1,000 games
    at once.

    Parameters:
        friendNameList: dict
            This is a dictionary containing person's profile names
            as key, and as values, a list (containing steamID, profile pictures,
            game libraries)

    Returns:
        friendNameList: dict
            This is a dictionary containing person's profile names
            as key, and as values, a list (containing steamID, profile pictures,
            game libraries (with price appended to game library))


    '''
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
    '''
    This function ties all the other functions within this file together (to
    simplify the data extraction process). For example, using this function
    would return the game library, profile picture, game price tied to a person's
    account.

    Parameters:
        steamId: int
            A 17 digit steam ID of your account, which could be found by
            navigating to your profile (in steamcommunity.com, navigate to top right
            corner, select view profile). After viewing your profile, in the url,
            your steamID could be found by the last 17 digits of your url.
            e.g. https://steamcommunity.com/profiles/76561197996661065/,
            76561197996661065 is the steam ID.

    Returns:
        prices: dict
            This is a dictionary containing person's profile names
            as key, and as values, a list (containing steamID, profile pictures,
            game libraries (with price appended to game library))


    '''
    try:
        friendId = get_friend_id(steamId)
        idAndName = get_friend_name(friendId)
        idNameLibrary = get_game_library(idAndName)
        prices = get_game_prices(idNameLibrary)
    except:
        print("Error occurred in loading data")
    return prices
