## Get a WordCloud graph of reviews 

```python
import APICall
import Reviews_Analysis as RA
#Set API call key 
APICall.set_key('3D41F12368AF3E305A8233ABFB965CA2')

#Obtain 1000 reviews for app with appid 413150
reviews_df = APICall.get_n_reviews(413150,10) # Appid, 1000 reviews
reviews_df_sentiments = RA.review_sentiments(reviews_df)

#Produce word cloud 
RA.reveiew_cloud(reviews_df_sentiments)
```

![word cloud](https://github.com/Sven-XinYuDong/SteamSMART/blob/main/Project%20Planning/Presentation/Cloud.png)





## Get the Sentiments Summary 

```python
#Label sentiments for each review 
reviews_df_sentiments = RA.review_sentiments(reviews_df)

import altair as alt # Summary with bar chart  
alt.Chart(reviews_df_sentiments).mark_bar().encode(
    alt.Y('sentiment'),
    
    alt.X('count()')).properties(title = 'Sentiments counts of the first 1000 review for Stardew Valley')


```

![Sentiments](https://github.com/Sven-XinYuDong/SteamSMART/blob/main/Project%20Planning/Presentation/Sentiments.png)

## Compare Genre preference with friends 

```python
# Get friend list (first four)
friend_list_first4 = list(APICall.get_friend_list('76561197996661065')['steamid'])[0:4]
# Pass obtained friend list to compare game genre preference 
id_genres = APICall.compare_genres_preference(friend_list_first4)

import altair as alt #Viz
alt.Chart(id_genres).mark_square(opacity = 0.9
).encode(
    alt.X('steamid',title = 'Genre'),
    alt.Y('genres',title = 'Palyer'),
    size='count()',
    color = 'count()'
).properties(width=150,title = 'Genre Preference Comparsion with Four Friends',height = 300)
```

![Sentiments](https://github.com/Sven-XinYuDong/SteamSMART/blob/main/Project%20Planning/Presentation/Genre%20Preference.png)

