''' 18-01-2020
    Shukrithi Rathna
    Assignment 2
    Q8. Generating Funnel Plot
'''

import plotly.express as px
data = dict(
    number=[50,110,250,180,70], 
    stage=["Requirement Elicitation","Requirement Anlaysis","Software Development","Debugging and Testing","Others" ])
fig = px.funnel(data, x='number', y='stage')
fig.show()
