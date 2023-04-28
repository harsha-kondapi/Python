# -*- coding: utf-8 -*-

import pandas as pd
import os

from pandas.core.frame import DataFrame


df = pd.read_csv('~/Downloads/application_stack_process (1)/application_stack_process.csv')


dataFrame = df[['workload_name','app_name']]

dup = dataFrame.drop_duplicates(subset=['workload_name','app_name'])



#print(dup)

dup.to_csv("app_to_server_mapping.csv")


#selectFrame2.to_csv("dependencies_with_unknown.csv")
#selectFrame4.to_csv("dependencies.csv")













