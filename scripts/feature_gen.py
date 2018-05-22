### helper functions to create features for the classification problem


from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as datetime


def binary_approval(rating):
    if rating > 50:
        return 1
    else:
        return 0

def speech_num_words(speech):
    return len(word_tokenize(speech))

def speech_num_sentences(speech):
    return len(sent_tokenize(speech))

def approval_features(all_df, speeches):
    for col in ['Approve', 'Disapprove']:
        for agg_type in ['mean', 'median', 'min', 'max', 'std']:
            new_col = '{}_{}'.format(col.lower(), agg_type)
            speeches[new_col] = pd.Series(list(round(all_df.groupby(['date'])[col].agg(agg_type), 3)), index=speeches.index)