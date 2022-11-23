
from dash.dependencies import Input, Output

from dash import Dash, html, dcc
import plotly.express as px
from plotly.express import line
import pandas as pd
from datetime import datetime


# dash_app = Dash(__name__)



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("final_data.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

print(df.head())
data = df.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization

line_chart = px.line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)
line_chart.update_layout(xaxis_title = 'Years',
                   yaxis_title = 'Sales in dollars',
                  title_text="Pink Morsel Sales "
                  )

line_chart.show()
# create the header
date=[df["date"]]
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)


# define the app layout
dash_app.layout =html.Div([

    dcc.RadioItems(df.region.unique(),df.region.unique()[1],id='region-names',)


        ])


    
if __name__ == '__main__':
    dash_app.run_server(debug=True)