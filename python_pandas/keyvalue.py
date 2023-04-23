import pandas as pd

calories = {'Day1' : 400,'Day2' : 380,'Day3' : 390}

myvar = pd.Series(calories, index=["Day1","Day2"])

print(myvar)

