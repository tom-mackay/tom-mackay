import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from threading import Thread
import time
import numpy as np

# Function to run the Dash app
def run_dash():
    app.run_server()

# Create a Dash application
app = dash.Dash(__name__)





# Load the OBJ file and extract vertices
with open('BASEmodel.obj', 'r') as f:
    lines = f.readlines()
vertices = []
for line in lines:
    parts = line.strip().split(' ')
    if parts[0] == 'v':
        vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
        vertices.append(vertex)
vertices = np.array(vertices)

obj_trace = go.Scatter3d(
    x=vertices[:, 0],
    y=vertices[:, 1],
    z=vertices[:, 2],
    mode='markers',
    marker=dict(
        size=1,
        color='blue',
    ),
)
# Create the figure
fig = go.Figure(data=[obj_trace])


# Define parallel traces
# trace1 = go.Scatter3d(
#     x=[1, 2, 3, 4, 5],
#     y=[0, 0, 0, 0, 0],
#     z=[10, 11, 12, 13, 14],
#     mode='markers+lines',
#     marker=dict(size=5, color='red'),
#     line=dict(width=2, color='red'),
#     name="Test Trace 01"
# )
# trace2 = go.Scatter3d(
#     x=[1, 2, 3, 4, 5],
#     y=[1, 1, 1, 1, 1],
#     z=[10, 11, 12, 13, 14],
#     mode='markers+lines',
#     marker=dict(size=5, color='blue'),
#     line=dict(width=2, color='blue'),
#     name="Test Trace 02"
# )
# trace3 = go.Scatter3d(
#     x=[1, 2, 3, 4, 5],
#     y=[2, 2, 2, 2, 2],
#     z=[10, 11, 12, 13, 14],
#     mode='markers+lines',
#     marker=dict(size=5, color='green'),
#     line=dict(width=2, color='green'),
#     name="Test Trace 03"
# )
# Create the figure and add the traces
# fig = go.Figure(data=[trace1, trace2, trace3])


fig.update_layout(
    scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=1)),
    # Set a margin of x pixels on each side
    margin=dict(l=15, r=15, b=15, t=15),
    legend=dict(
        x=1.1,
        y=0.5,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        # Add Border to legend
        #bgcolor="LightSteelBlue",
        #ordercolor="Black",
        #borderwidth=2
        tracegroupgap=10

    ),
    width=750,  # Set the width of the plot
)

# Calculate 95% of the original width and height
new_width = int(0.95 * 600)
new_height = int(0.95 * 450)

app.layout = html.Div([
    dcc.Graph(id='my-graph', figure=fig, style={'width': f'{new_width}px', 'height': f'{new_height}px'})
])









# Start the Dash app in a separate thread
dash_thread = Thread(target=run_dash)
dash_thread.daemon = True
dash_thread.start()

# Wait for the Dash app to start
time.sleep(2)







# PyQt5 Application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Plotly Plot in PyQt5")
        self.setGeometry(100, 100, 800, 600) # X, Y and W and H

        # Create a QWebEngineView and set the Dash app URL
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:8050"))
        self.browser.setFixedSize(600, 450)


        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Run the PyQt5 application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())