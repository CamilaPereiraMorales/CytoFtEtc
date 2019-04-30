import json

import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': 20*long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 1, 118.25),
        ('nyc', 'New York', 2, 74),
        ('to', 'Toronto', 3, 79.38),
        ('mtl', 'Montreal', 4, 73.57),
        ('van', 'Vancouver', 5, 123.12),
        ('chi', 'Chicago', 6, 87.63),
        ('bos', 'Boston', 7, 71.06),
        ('hou', 'Houston', 8, 95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'bos'),
        ('to', 'hou'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

elements = nodes + edges

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'label': 'data(label)'
        }
    }
]


app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-event-callbacks',
        layout={'name': 'preset'},
        elements=elements,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    ),
    html.Div(id='cytoscape-tapNodeData-output')
])



@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              [Input('cytoscape-event-callbacks', 'tapNodeData')])
def displayTapNodeData(data):
    if data:

                return dcc.Graph(
                    id="cytoscape-tapNodeData-output",
                    figure={
                        'data': [
                            {
                                "x": elements['x'],
                                "y": elements['y'],
                                "text": elements['label'],
                                "type":"bar",

                            }
                        ]
                    }
                )



if __name__ == '__main__':
    app.run_server(debug=True) 
