import pandas as pd

def friendlist_to_dataframe(friendNameList):
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

    dataframe = dataframe.melt(["Name", "ProfilePicture", "GameList"])



    dataframe["Text"] = (["Total number of games owned"] * dataframe["variable"].value_counts()[0]
                         + ["Total amount of games owned with zero playtime"] * dataframe["variable"].value_counts()[0]
                         + ["Total amount of dollars spent on games ($CAD)"] * dataframe["variable"].value_counts()[0]
                         + ["Total number of minutes spent playing games"] * dataframe["variable"].value_counts()[0]
                     )
    return dataframe
