import pandas as pd

data = {
    'Day' : [1,2,3,4,5,6,7,8,9,10],
    'Visitors' : [18,26,18,19,20,11,18,18,24,13],
    'Bounce_Rate' : [77.27, 74.07, 73.68, 65, 90, 70, 72, 62.16, 81.25, 72],
    }
df = pd.DataFrame(data)

print(df)


    