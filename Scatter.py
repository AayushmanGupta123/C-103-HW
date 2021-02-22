import pandas as pd
import plotly.express as px

file = pd.read_csv("data1.csv")
fig = px.scatter(file,x = "date",y = "cases",color = "country", title = "Covid-19 Cases In Different Countries")
fig.show()