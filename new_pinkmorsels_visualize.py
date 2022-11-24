
from dash.dependencies import Input, Output

from dash import Dash, html, dcc
import plotly.express as px
from plotly.express import line
import pandas as pd
from datetime import datetime


dash_app = Dash(__name__)



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv("final_data.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}
#print(df.head())
data = df.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization

def generate_figure(data):
    line_chart = px.line(data, x="date", y="sales")
    
    line_chart.update_layout(xaxis_title = 'Years',
                    yaxis_title = 'Sales in dollars',
                    title_text="Pink Morsel Sales ",
                    plot_bgcolor=COLORS["secondary"],
                    paper_bgcolor=COLORS["primary"],
                    font_color=COLORS["font"],
                    )

    return line_chart

visualization = dcc.Graph(
        id="visualization",
        figure=generate_figure(data)
    )
# create the header

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


# define the region picker callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
dash_app.layout =html.Div(
    [

        header,
        visualization,
        region_picker_wrapper

        ],
        style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
        )


    
if __name__ == '__main__':
    dash_app.run_server(debug=True)