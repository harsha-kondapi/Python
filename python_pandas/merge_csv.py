# importing pandas
import pandas as pd

# merging csv files
df = pd.concat(
	map(pd.read_csv, ['dependencies.csv', 'known_to_unknown.csv','unknown_to_known.csv','unknown_to_unknown.csv']), ignore_index=True)
#print(df)
df.to_csv("test.csv")
