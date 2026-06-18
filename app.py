"""
app.py
Archivo principal del Dashboard de Calidad del Agua.
Pestañas: Contexto del Problema, EDA, Metodología
"""

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from tabs.contextoproblema import layout as layout_contexto
from tabs.eda               import layout as layout_eda
from tabs.metodologia       import layout as layout_metodologia

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        "https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap",
    ],
    suppress_callback_exceptions=True,
    title="💧 Water Quality Dashboard",
)
server = app.server

NAVBAR_STYLE = {
    "background"  : "linear-gradient(135deg, #AED9E0 0%, #B5EAD7 100%)",
    "boxShadow"   : "0 2px 8px rgba(0,0,0,0.12)",
    "borderBottom": "none",
}
TAB_STYLE = {
    "fontWeight"    : "600",
    "fontSize"      : "0.85rem",
    "padding"       : "10px 18px",
    "borderRadius"  : "8px 8px 0 0",
    "border"        : "none",
    "color"         : "#555",
    "backgroundColor": "#f0f4f7",
}
TAB_SELECTED_STYLE = {
    **TAB_STYLE,
    "backgroundColor": "#ffffff",
    "color"          : "#2c3e50",
    "borderTop"      : "3px solid #AED9E0",
}

app.layout = html.Div([

    dbc.Navbar(
        dbc.Container([
            html.Span("💧", style={"fontSize": "1.8rem", "marginRight": "10px"}),
            dbc.NavbarBrand("Water Quality Dashboard",
                            style={"fontWeight": "700",
                                   "fontSize"  : "1.25rem",
                                   "color"     : "#2c3e50"}),
        ], fluid=True),
        style=NAVBAR_STYLE, className="mb-0 py-2",
    ),

    dbc.Container([
        dcc.Tabs(
            id="main-tabs",
            value="tab-contexto",
            children=[
                dcc.Tab(label="🏠 Contexto",    value="tab-contexto",
                        style=TAB_STYLE, selected_style=TAB_SELECTED_STYLE),
                dcc.Tab(label="📊 EDA",         value="tab-eda",
                        style=TAB_STYLE, selected_style=TAB_SELECTED_STYLE),
                dcc.Tab(label="🔬 Metodología", value="tab-metodologia",
                        style=TAB_STYLE, selected_style=TAB_SELECTED_STYLE),
            ],
            style={"marginTop": "16px", "border": "none"},
            colors={"border": "transparent", "primary": "#AED9E0",
                    "background": "transparent"},
        ),
        html.Div(id="tab-content",
                 style={"backgroundColor": "#f8fafc",
                        "minHeight"      : "calc(100vh - 120px)",
                        "borderRadius"   : "0 0 12px 12px",
                        "boxShadow"      : "0 2px 8px rgba(0,0,0,0.06)"}),
    ], fluid=True, style={"padding": "0 24px"}),

], style={"backgroundColor": "#f0f4f7", "minHeight": "100vh",
          "fontFamily": "'Segoe UI', sans-serif"})


@app.callback(
    Output("tab-content", "children"),
    Input("main-tabs", "value"),
)
def render_tab(tab: str):
    if tab == "tab-contexto":
        return layout_contexto()
    elif tab == "tab-eda":
        return layout_eda()
    elif tab == "tab-metodologia":
        return layout_metodologia()
    return html.Div("Pestaña no encontrada.")


if __name__ == "__main__":
    app.run(debug=True, port=8050)
