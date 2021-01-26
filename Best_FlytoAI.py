import pandas as pd
data = pd.read_csv('data_analytics.csv')

RESULT  = ((data.groupby(['Subscriber ID']).apply(len) - 1)*9.99*0.7).reset_index()
RESULT = RESULT.rename(columns={0:'LTV'})

print(RESULT.LTV.mean())