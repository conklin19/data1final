## Code Louisville ##
## Data 1 Final Project ##
## Adam Conklin ##
## Analyzing KenPom Data for NCAA Final Four Teams ##

import matplotlib as mp
import pandas as pd
import seaborn as sns


##Requirement 1.2 Read-In local csv using pandas ###
df = pd.read_csv('assets\KPdata.csv')

data = df
##Requirement 2.1 remove null values ###
##Delete 2020 because NO TOURNAMENT due to COVID-19##
###Delete the 4 rows where the 2020 Final Four teams woud have been###
data = data[data.Year != 2020]  
avg = float(data.KPvalue.mean())
print(avg)
maxKPvalue = float(data[['KPvalue']].max())
print(maxKPvalue)


