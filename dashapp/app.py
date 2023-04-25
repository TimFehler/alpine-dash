import pandas as pd
from dash import Dash, dcc, html

app = Dash(__name__)



app.layout = html.Div()


if __name__ == "__main__":
    app.run_server(debug=True)