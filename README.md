# State of the Union Address Text Analysis

## Text Mining for Public Policy, Spring 2018

## Project Goal
The high-level goal of this project is to apply text analysis techniques, including sentiment analysis and topic modeling, to State of the Union addresses. To add to the existing body of work that already accomplishes these goals, an extension of the project is to determine whether sentiment analysis of State of the Union addresses can be used to predict presidential approval.   

## Data
UCSB’s [The American Presidency Project](http://www.presidency.ucsb.edu/sou.php)
- Corpus built by scraping State of the Union transcripts
- Output stored as .txt file for each address, including both written and spoken addresses

Roper Center for Public Opinion Research [Presidential Approval Project](https://presidential.roper.center/)
- Database of public presidential polls starting from 1942 


## File Structure

    ├── scripts			
    │   ├── approval.py           # Code for aggregating historical polls
    │   ├── evaluate.py           # Helpfer functions to plot confusion matrix
    │   ├── feature_gen.py        # Scripts to generate features for predicting approval
    │   ├── sentiment_analyzer.py # Analyze sentiment of speeches 
    │   └── sotu_scraper.py       # Webscraping to obtain speech corpus
    │
    ├── sentiment_analysis.ipynb  # Notebook for analyzing SoTU sentiment scores
  	│  
    ├── approval_analysis.ipynb   # Notebook for approval data preprocessing and feature generation
  	│  
    ├── models.ipynb              # Notebook for model fitting, selection, and evaluation
 	│ 
    ├── bigram_analysis.ipynb     # Notebook for text bigram analysis
    │  
    ├── topic_modeling.ipynb      # Notebook for text topic modeling using LDA, making word clouds
    │
    ├── tmpp-presentation.pdf     # Project presenation, (5/29/18)
    │  
    └── README.md

## References
1. Pablo Martinez Monsivais/Getty Images, [State of the Union Photo Gallery](http://www.wbur.org/hereandnow/2016/01/11/obama-first-congressional-address)
2. Jonathan Bouchet, [NLP analysis on the SOTU addresses](https://www.kaggle.com/jonathanbouchet/nlp-analysis-on-the-sotu-addresses)
3. Jennifer Dixon, [Presidential Speech Analysis](https://github.com/jennifro/Feeling-Presidential)
4. Frank Evan, [Topic Modeling of the State of the Union Address](https://dzone.com/articles/topic-modeling-the-state-of-the-union-address-with)
5. FiveThirtyEight,  [Presidential approval poll aggregator](https://projects.fivethirtyeight.com/trump-approval-ratings/?ex_cid=rrpromo)
6. UCSB, [The American Presidency Project](http://www.presidency.ucsb.edu/sou.php)
7. Roper Center for Public Opinion Research, [Presidential Approval Project](https://presidential.roper.center/)




