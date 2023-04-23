import pandas as pd

#pd.options.display.max_rows = 9999

df= pd.read_csv('data.csv')

dataframe = df[['Duration','Pulse','Maxpulse','Calories']]

#selectframe = dataframe.loc[dataframe['Pulse'] != dataframe['Maxpulse']]

#selectframe1 = selectframe.loc[selectframe['Duration'] != selectframe['Calories']]

#print(selectframe1)

#print(selectframe)

#print(dataframe)

dataframe.to_csv("files.csv")

#print(df)

#print(df.head(10))

#print(df.info())

#print(pd.options.display.max_rows)