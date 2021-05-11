import pandas as pd
df=pd.read_csv('data.csv')
groupeddf=df.groupby(['Item No.','Location Code'])
print(groupeddf.first())