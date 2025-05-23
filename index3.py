import dash
from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

# Criar um gráfico de exemplo com template escuro
fig = px.scatter(x=[1, 2, 3], y=[4, 1, 6])
fig.update_layout(template='plotly_dark')

app.layout = html.Div([
    html.Div([
        # Coluna 1: Texto
        html.Div([
            html.H3("Sales Analytics"),
            html.P("Aqui vai um resumo do desempenho.")
        ], style={"background": "#444", "color": "#fff", "height": "25vh", "padding": "10px"}),

        # Coluna 2: Gráfico
        html.Div([
            dcc.Graph(figure=fig, config={"displayModeBar": False})
        ], style={"background": "#666", "height": "25vh", "padding": "10px"}),

        # Coluna 3: Botão
        html.Div([
            html.H5("Escolha o Mês"),
            dbc.Button("Clique Aqui", color="primary")
        ], style={"background": "#888", "color": "#fff", "height": "40vh", "padding": "10px"}),

        # Encaixado abaixo: outro gráfico
        html.Div([
            dcc.Graph(figure=fig, config={"displayModeBar": False})
        ], style={"background": "#aaa", "height": "15vh", "padding": "10px", "gridColumn": "1 / span 2"})
    ], style={
        "display": "grid",
        "gridTemplateColumns": "repeat(auto-fit, minmax(250px, 1fr))",
        "gap": "10px"
    })
], style={"padding": "20px"})

if __name__ == '__main__':
    app.run(debug=True, port=8051)


