import pandas as pd

data = {
    'calories' : [400,380,390],
    'Duration' : [40,50,60]
    }
  #Load Data into DataFrame Object  
df = pd.DataFrame(data)

print(df)

#print(df.loc[0])

#print(df.loc[[1,2]])