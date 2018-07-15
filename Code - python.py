# -*- coding: utf-8 -*-
"""
#Created on Tue Jul 10 23:06:27 2018

#@author: lohit
#"""
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sid = SIA()



input_file = "D://Desktop//4th term//Digital and Social Media Analytics//Project//new.xlsx" 
output_file ="D://Desktop//4th term//Digital and Social Media Analytics//Project//Output1.csv"
out_df = pd.DataFrame()

df = pd.read_csv(input_file,encoding ='utf-8')
df = df.fillna(" ")
col_names = list(df.columns.values)

for col in col_names:
    data = df[col].tolist()
    compound = []
    #negative = []
    #neutral = []
    #positive = []
    for sentence in data:
        ss = sid.polarity_scores(sentence) 
        compound.append(ss['compound'])
        #    negative.append(ss['neg'])
        #    neutral.append(ss['neu'])
        #    positive.append(ss['pos'])
    
    out_df[col] = compound
    #df['Negative'] = negative
    #df['Neutral'] = neutral
    #df['Positive'] = positive

out_df.to_csv(output_file,index=False)
