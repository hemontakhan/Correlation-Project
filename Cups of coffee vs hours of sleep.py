import csv
import plotly.express as px

with open('cups of coffee vs hours of sleep.csv') as r:
    data = csv.DictReader(r)
    fig = px.scatter(data,x="Coffee in ml",y="sleep in hours")
    
fig.show()