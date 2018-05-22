# approval ratings helper scripts


from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as datetime


xls_file = pd.ExcelFile('data/approval_ratings.xls')


sheet_list = []
for sheet in xls_file.sheet_names:
    df = xls_file.parse(sheet)
    df['Name'] = pd.Series([sheet]*len(df), index=df.index)
    sheet_list.append(df)


combined_df = pd.concat([sheet for sheet in sheet_list], ignore_index=True)
combined_df['Polling Start'] = pd.to_datetime(combined_df['Polling Start'])
combined_df['Polling End'] = pd.to_datetime(combined_df['Polling End'])


def get_rating_subset(speech, rating):
    temp_df = pd.DataFrame()
    for i, speech_row in speech.iterrows():
        for j, rating_row in rating.iterrows():
            if speech_row['date'] >= (rating_row['Polling Start'] - pd.Timedelta(days=14)) and speech_row['date'] <= (rating_row['Polling End'] + pd.Timedelta(days=14)):
                data = rating_row[['Name', 'Polling Start', 'Polling End', 'Approve', 'Disapprove']]
                temp_df = temp_df.append(data)
    temp_df.to_csv('data/apporvals_subset.csv', index=False)
    return temp_df