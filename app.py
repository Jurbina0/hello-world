import dash
from dash import Dash, html, dcc

# Aplicación Dash
# Inicializamos la aplicación Dash
app = Dash(__name__, use_pages=True)

# Diseñamos el layout de la aplicación
app.layout = html.Div([
    html.H1('Malentendidos, prensa y números'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

# Preparamos la ejecución de la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)