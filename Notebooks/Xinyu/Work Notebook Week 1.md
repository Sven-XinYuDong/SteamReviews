# Work Notebook Week 1

## 2023/1/19

- Reviewed the Demo data get from two potential APIs together 
- Decided the work path together 
  - Work on the reviews to produce bags of word visualization 
  - if too hard：
    - return back to statistical graphs for numerical attributes (review number, review date etc )

## 2023/1/20

- Search for proper packages to do the frequency of the words and do the correspondent visualization.
  - sikitlearn package `CountVectorizer()` function 
  - TextBlob package `SentimentIntensityAnalyzer()`to get a simple sentiment outcome and visualization.
- Decide to implement a simple sentimental analysis for the review 
- Create the GitHub link repository for this project, upload the log, create the folder structure
- Create a Jupiter notebook to go through the process to:
  - get the `request ` source rough data
  - covert to  pandas dataframe 
  - clean the reviews (remove symbols and lower cases)
  - run the two packages to obtain a draft 