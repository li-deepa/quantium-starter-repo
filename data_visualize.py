from dash import Dash, html, dcc
import plotly.express as px
from plotly.express import line
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("final_data.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

print(df.head())
data = df.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization

line_chart = px.line(data, x="date", y="sales", title="Pink Morsel Sales",color='region')
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)
line_chart.update_layout(xaxis_range=['2021-01-14','2021-01-16'],
                  title_text="Pink Morsel Sales before and after january 15th 2021")
line_chart.show()
# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)