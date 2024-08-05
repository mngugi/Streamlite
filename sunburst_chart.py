import plotly.express as px

data = {
    'userName': [ "Angel", "Ben", "Cat", "Dougie", "Eve", "Father", "Gloria"],
    'Value': [10,15,9,18,20,10,13],

         }

figure = px.sunburst(data, names = 'userName', values= 'value')

