import pandas as pd
import plotly.express as px

df = pd.read_csv('ETH_USD_2018-12-13_2019-12-08-CoinDesk.csv')

fig = px.line(df, x = 'Date', y = '24h High (USD)', title='ETH максимумы за год')
fig.show()