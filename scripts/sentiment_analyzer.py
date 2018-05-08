#######################
#   sotu setntiment   #
#######################


import nltk
import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def calc_sentiment_scores(df):
    '''
    Takes a dataframe of speeches and returns vader sentiment scores for each speech
    '''
    analyser = SentimentIntensityAnalyzer()
    compound_score = []
    positive_score = []
    neutral_score = []
    negative_score = []
    
    for speech in df.speech:
        snt_dict = {
            'compound':[],
            'pos':[],
            'neg':[],
            'neu':[]
        }
        for sent in sent_tokenize(speech):
            snt = analyser.polarity_scores(sent)
            snt_dict['compound'].append(snt['compound'])
            snt_dict['pos'].append(snt['pos'])
            snt_dict['neg'].append(snt['neg'])
            snt_dict['neu'].append(snt['neu'])
            
        compound_score.append(np.mean(snt_dict['compound']))
        positive_score.append(np.mean(snt_dict['pos']))
        negative_score.append(np.mean(snt_dict['neg']))
        neutral_score.append(np.mean(snt_dict['neu']))
            
    df['compound'] = pd.Series(compound_score,  index=df.index)
    df['positive'] = pd.Series(positive_score,  index=df.index)
    df['negative'] = pd.Series(negative_score,  index=df.index)
    df['neutral'] = pd.Series(neutral_score,  index=df.index)
    
    return df


if __name__ == '__main__':
	in_file = open(sys.argv[1], 'w') if len(sys.argv) > 1 else 'sotu_content.pkl'
	out_file = open(sys.argv[-1], 'w') if len(sys.argv) >= 2 else 'sotu_sentiment_scores.pkl'
	
	speeches = pd.read_pickle(in_file)
	speeches['date'] = pd.to_datetime(speeches['date'])
	speeches = speeches[~speeches.duplicated(subset='date')]
	out_df = calc_sentiment_scores(speeches)
	out_df.to_pickle(out_file)