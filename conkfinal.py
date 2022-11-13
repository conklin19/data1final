## Code Louisville ##
## Data 1 Final Project ##
## Adam Conklin ##
## Analyzing KenPom Data for NCAA Final Four Teams ##

import pandas as pd
import seaborn as sns
import matplotlib as mp

df = pd.read_csv('assets\KPdata.csv')

data = df
data = data[data.Year != 2020]
print(data)

print(df)
