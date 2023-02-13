import pandas as pd

def friendlist_to_dataframe(friendNameList):
    '''
    This function converts the raw data extracted from Steam into a dataframe
    format.

    Parameters:
        dict: friendNameList
            This is the data source that has been obtained by the extract_data
            function, or alternatively the get_game_prices function in the
            SteamDataExtraction module (and is structured to be in a specific
            format. See SteamDataExtract for more details.)

    Returns:
        Steam dataframe: Pandas dataframe
            Pandas dataframe containing Steam information (e.g. prices of games,
            person name)
    '''
    fullLst = []

    for friend in friendNameList:
        lst = []
        lst.append(friend) #Append friend name to list
        lst.append(friendNameList[friend][1]) #Append friend avatar to list

        gameLst = [] #Start appending library of games to list
        for game in friendNameList[friend][2]:
            gameLst.append(game["name"])
        lst.append(gameLst) #End appending library of games to list

        totalNumGamesOwned = len(gameLst) #Append total number of games owned
        lst.append(totalNumGamesOwned)


        zeroPlaytimeGames = 0 #Append total number of games owned with zero playtime
        for game in friendNameList[friend][2]:
            if game["playtime_forever"] == 0:
                zeroPlaytimeGames += 1
        lst.append(zeroPlaytimeGames)


        priceLst = []
        for game in friendNameList[friend][2]:
            try:
                priceLst.append(game["price"])
            except:
                pass
        #lst.append(priceLst) #Append purchase price (full price, not on sale) for all games owned

        try:
            lst.append(sum(priceLst)) #Uncomment this line if we want the sum of prices for all games owned instead of individual items
        except:
            pass

        playtimeLst = []
        for game in friendNameList[friend][2]:
            playtimeLst.append(game["playtime_forever"])
        #lst.append(playtimeLst) #Appending total playtime for all games owned
        lst.append(sum(playtimeLst))






        fullLst.append(lst)
    return pd.DataFrame(fullLst, columns = ["Name", "ProfilePicture", "GameList", "TotalNumGames", "ZeroPlaytimeGames", "GamePrice", "Playtime"])



def chart_dataframe(dataframe):
    '''
    This function takes a dataframe containing Steam information and transforms
    it into the format required for plotting interactive dashboards.

    Parameters:
        dataframe: Pandas dataframe
            Pandas dataframe containing Steam information (e.g. prices of games,
            person name)
    Returns:
        dataframe: Transformed Pandas dataframe
            Pandas dataframe that has been transformed (e.g. melted certain columns)
            into a format ready plotting building interactive dashboards.
    '''
    dataframe = dataframe.melt(["Name", "ProfilePicture", "GameList"])



    dataframe["Text"] = (["Total number of games owned"] * dataframe["variable"].value_counts()[0]
                         + ["Total amount of games owned with zero playtime"] * dataframe["variable"].value_counts()[0]
                         + ["Total amount of dollars spent on games ($CAD)"] * dataframe["variable"].value_counts()[0]
                         + ["Total number of minutes spent playing games"] * dataframe["variable"].value_counts()[0]
                     )
    return dataframe
