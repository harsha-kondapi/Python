# -*- coding: utf-8 -*-

import pandas as pd
import os

from pandas.core.frame import DataFrame


df = pd.read_csv('~/Downloads/random.csv')

#dataFrame = df[['src_name','src_group','src_addr','src_port','dest_name','dest_group','dest_addr','dest_port','protocol_name']]

dataFrame = df[['src_name','src_group','src_addr','dest_name','dest_group','dest_addr']]

selectFrame = dataFrame.loc[dataFrame['src_addr'] != dataFrame['dest_addr']]   # no self dependency 
selectFrame1 = selectFrame.loc[selectFrame['src_name'] != selectFrame['dest_name']] # no self dependency
selectFrame2 = selectFrame1.loc[selectFrame1['src_group'] != selectFrame1['dest_group']] # no self dependency

selectFrame3 = selectFrame2.loc[selectFrame2['src_group'] != 'none']
selectFrame4 = selectFrame3.loc[selectFrame3['dest_group'] != 'none']

'''
# no self dependency - output
-----------------------------
print(selectFrame4)
selectFrame4.to_csv("slc_dependencies.py")
'''

'''
# no duplicates & self dependency - output
------------------------------------------
nodupself = selectFrame4.drop_duplicates(subset=['src_name','src_group','src_addr','dest_name','dest_group','dest_addr'])
nodupself.to_csv("slc_dependencies1.csv")
'''


#selectFrame2.to_csv("dependencies_with_unknown.csv")






























