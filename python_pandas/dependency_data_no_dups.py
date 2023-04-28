
import pandas as pd
import os

from pandas.core.frame import DataFrame


df= pd.read_csv('~/Downloads/dependency_data/dependency_data.csv')
dataFrame=df[['src_name','src_group','src_addr','dest_name','dest_group','dest_addr']]

#[['src_name','src_group','src_addr','src_port','dest_name','dest_group','dest_addr','dest_port','protocol_name']]


selectFrame = dataFrame.loc[dataFrame['src_addr']!=dataFrame['dest_addr']]
selectFrame1=selectFrame.loc[selectFrame['src_name']!=selectFrame['dest_name']]
selectFrame2=selectFrame1.loc[selectFrame1['src_group']!=selectFrame1['dest_group']]
selectFrame3=selectFrame2.loc[selectFrame2['src_group']!='none']
selectFrame4=selectFrame3.loc[selectFrame3['dest_group']!='none']

#selectFrame4.groupby(["dest_addr","src_addr"]).nth(0)

selectFrame4 = selectFrame4.drop_duplicates(subset=['dest_addr'])

#selectFrame4.to_csv("dependency_no_dups.csv")

#print(selectFrame4)