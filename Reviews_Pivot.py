### This module provides Sentiments Labeling for each Steam Reviews and WordCloud Visulization

### Dependencies
import pandas as pd
import numpy as np
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk #nltk.downloader.download('vader_lexicon')
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def Review_Sentiments_Labeling(df):
    '''
    This function will label each steam review with polarity, subjectivity and sentiment.

    Parameters:
        df: - A pandas Dataframe of Steam reviews details

    Rerurn:
        A expanded Dataframe with three new Column: polarity, subjectivity and sentiment
    '''

    df[['polarity', 'subjectivity']] = df['review'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))

    for index, row in df['review'].iteritems():
        score = SentimentIntensityAnalyzer().polarity_scores(row)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        if neg > pos:
            df.loc[index, 'sentiment'] = "Negative"
        elif pos > neg:
            df.loc[index, 'sentiment'] = "Positive"
        else:
            df.loc[index, 'sentiment'] = "neutral"

    return df


def Reveiew_Cloud_Glimpse(df):
    '''
    Plot a simple WordCloud for users to have a glimpse of the reveiws of a game.
    '''
    comment_words = ''
    stopwords = set(STOPWORDS)


    for val in df.review:
        tokens = val.split()
        comment_words += " ".join(tokens)+" "

    wordcloud = WordCloud(width = 800,height = 800,
                background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize = (4, 4), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    plt.show()
