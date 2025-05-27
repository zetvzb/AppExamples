import dash 
from dash import html, dcc

import pandas as pd 
import numpy as np
import plotly.express as px 

# Generate sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=10),
    'Sales': np.random.randint(20, 150, size=10)
})

# Create bar chart with hover info
fig = px.bar(
    data, 
    x='Date', 
    y='Sales', 
    title='📊 Daily Sales Overview',
    color='Sales', 
    color_continuous_scale='Blues',
    hover_data={'Date': True, 'Sales': True}
)

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2("📦 Business Dashboard Example"),
    html.P("A Dash app that displays a sales bar chart with color scale and summary stats."),
    dcc.Graph(figure=fig),
    
    html.H4("🔢 Summary Stats"),
    html.Ul([
        html.Li(f"Total Sales: {data['Sales'].sum()}"),
        html.Li(f"Average Sales: {data['Sales'].mean():.2f}"),
        html.Li(f"Max Sales: {data['Sales'].max()}"),
        html.Li(f"Min Sales: {data['Sales'].min()}")
    ])
])

if __name__ == '__main__':
    app.run(debug=True)

    # To Run App 
    #python dash_example_app.py