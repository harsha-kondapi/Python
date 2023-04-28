
import pandas as pd
import os

from pandas.core.frame import DataFrame


df= pd.read_csv('~/Downloads/test.csv')
dataFrame=df[['names','age','interests']]



#selectFrame = dataFrame.loc[dataFrame['names']!=dataFrame['age']]

dup = dataFrame.drop_duplicates(subset=['names','age','interests'])

#print(dup)

dup.to_csv("names.csv")