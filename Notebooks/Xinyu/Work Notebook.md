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
- Create the GitHub link repository for this project, upload the log, and create the folder structure
- Create a Jupiter notebook to go through the process to:
  - get the `request ` source rough data
  - covert to  pandas dataframe 
  - clean the reviews (remove symbols and lower cases)
  - run the two packages to obtain a draft 

## 2023/1/21

- Tried the WordCloud Package to get the word frequency visualization 

## 2023/1/22

- Read Sample WPI Warpers 
- Based on the `caRecall `  example we can design three parts in the main part;

## 2023/1/23

- Ask for additional Resources for Python API Wrapper 

## 2023/1/29

- Review the Python  file from Matt 
  - Matt gets the function of requesting a given number of entries to get the reviews.
- Upload two .py files: Steam_Review_Extraction and Review_Glimpse 
- Use the two python module in the Function test file and confirm both works well
- Discuss and decide on closing the development of Implementation 2 

## 2023/1/30

- Discuss the Implementation 2: 
  - Conclusion: Doing the Profile Analysis 


## 2023/2/3

- Refine all demo functions to `APICall` module with docstrings, and parameters with improved usability.

## 2023/2/4

- Edit the Viz Module to produce a better cross plot than a simple bar chart.
- Tried to capsule all functions in class but decide to keep them as functions.

## 2023/2/5

- Discuss the presentation 
- Produce the Slides for the technique Part of Profile Analysis and Review Analysis 
- Confirm the Presentation materials 

## 2023/2/6

- Add Try Except to APIcall.py 
- Add Unitest for  APIcall.py
- Integrate uni-test to Testsuite of Profile Analysis 

## 2023/2/7

- Add travis CI confiuration 

## 2023/2/8

- Add Review Analysis part into Vegette 
