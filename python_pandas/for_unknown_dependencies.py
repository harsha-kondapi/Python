import pandas as pd
import os

from pandas.core.frame import DataFrame

df= pd.read_csv('~/Downloads/detailed_application_dependency_data (10)/detailed_application_dependency_data.csv')
dataFrame = df[['src_name','src_group','src_addr','src_port','dest_name','dest_group','dest_addr','dest_port','protocol_name']]

selectFrame = dataFrame.loc[dataFrame['src_addr'] != dataFrame['dest_addr']] # no self dependency

''' 1st condition for unknown dependencies (unknown_to_known)'''
selectFrame1 = selectFrame.loc[selectFrame['src_name'] == 'unknown'] #src_name is 'unknown' 
selectFrame2 = selectFrame1.loc[selectFrame1['dest_name'] != 'unknown'] #dest_name is 'known'
#print(selectFrame2.loc[selectFrame2['dest_port'].isin([80,443,1433])].to_string()) #for printing values on the cmd. 'to.string()' method is used to print all rows in the cmd
frame1 = selectFrame2.loc[selectFrame2['dest_port'].isin([80,443,1433,3306,5432])]
frame1.to_csv("unknown_to_known.csv")

'''2nd condition for unknown dependencies (unknown_to_unknown)'''
selectFrame3 = selectFrame.loc[selectFrame['src_name'] == 'unknown'] #src_name is 'unknown'
selectFrame4 = selectFrame3.loc[selectFrame3['dest_name'] == 'unknown'] #dest_name is 'unknown'
#print(selectFrame4.loc[selectFrame4['dest_port'].isin([80,443,1433])].to_string())
frame2 = selectFrame4.loc[selectFrame4['dest_port'].isin([80,443,1433,3306,5432])]
frame2.to_csv("unknown_to_unknown.csv")

'''3rd condition for unknown dependencies (known_to_unknown)'''
selectFrame5 = selectFrame.loc[selectFrame['src_name'] != 'unknown'] #src_name is 'known'
selectFrame6 = selectFrame5.loc[selectFrame5['dest_name'] == 'unknown'] #dest_name is 'unknown'
#print(selectFrame6.loc[selectFrame6['dest_port'].isin([80,443,1433])].to_string())
frame3 = selectFrame6.loc[selectFrame6['dest_port'].isin([80,443,1433,3306,5432])]
frame3.to_csv("known_to_unknown.csv")



