import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from threading import Thread
import time
import numpy as np
import pandas as pd

# Function to run the Dash app
def run_dash():
    app.run_server()

# Create a Dash application
app = dash.Dash(__name__)


# Test - Different Data 
# theta = np.linspace(0, 2*np.pi, 100)
# df1 = pd.DataFrame({'r': np.sin(3*theta), 'theta': theta, 'z': np.cos(3*theta)})
# df2 = pd.DataFrame({'r': np.sin(2*theta), 'theta': theta, 'z': np.cos(2*theta)})
# df3 = pd.DataFrame({'r': np.sin(theta), 'theta': theta, 'z': np.cos(theta)})
# # Align frames to create a 3D array
# frames = [df1, df2, df3]
# max_len = max(len(frame) for frame in frames)
# for frame in frames:
#     frame = frame.reindex(range(max_len)).interpolate(method='linear')
# # Plot the 3D array with all markers connected by lines
# fig = go.Figure()
# for frame in frames:
#     fig.add_trace(go.Scatter3d(
#         x=frame['r']*np.cos(frame['theta']),
#         y=frame['r']*np.sin(frame['theta']),
#         z=frame['z'],
#         mode='markers+lines'
#     ))
# fig.show()







# Define parallel traces
trace1 = go.Scatter3d(
    x=[1, 2, 3, 4, 5],
    y=[0, 0, 0, 0, 0],
    z=[10, 11, 12, 13, 14],
    mode='markers+lines',
    marker=dict(size=5, color='red'),
    line=dict(width=2, color='red'),
    name="Test Trace 01"
)
trace2 = go.Scatter3d(
    x=[1, 2, 3, 4, 5],
    y=[1, 1, 1, 1, 1],
    z=[10, 11, 12, 13, 14],
    mode='markers+lines',
    marker=dict(size=5, color='blue'),
    line=dict(width=2, color='blue'),
    name="Test Trace 02"
)
trace3 = go.Scatter3d(
    x=[1, 2, 3, 4, 5],
    y=[2, 2, 2, 2, 2],
    z=[10, 11, 12, 13, 14],
    mode='markers+lines',
    marker=dict(size=5, color='green'),
    line=dict(width=2, color='green'),
    name="Test Trace 03"
)


# # Create the figure and add the traces
# fig = go.Figure(data=[trace1, trace2, trace3])

# fig.update_layout(
#     scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=1)),
#     # Set a margin of x pixels on each side
#     margin=dict(l=15, r=15, b=15, t=15),
#     legend=dict(
#         x=1.1,
#         y=0.5,
#         traceorder="normal",
#         font=dict(
#             family="sans-serif",
#             size=12,
#             color="black"
#         ),
#         # Add Border to legend
#         #bgcolor="LightSteelBlue",
#         #ordercolor="Black",
#         #borderwidth=2
#         tracegroupgap=10

#     ),
#     width=750,  # Set the width of the plot
# )







# Create the figure and add the traces
fig = go.Figure(data=[trace1, trace2, trace3])

# Add lines connecting the markers of the three traces
for i in range(len(trace1['x'])):
    fig.add_trace(go.Scatter3d(
        x=[trace1['x'][i], trace2['x'][i], trace3['x'][i], trace1['x'][i]],
        y=[trace1['y'][i], trace2['y'][i], trace3['y'][i], trace1['y'][i]],
        z=[trace1['z'][i], trace2['z'][i], trace3['z'][i], trace1['z'][i]],
        mode='lines',
        line=dict(color='black', width=2),
        showlegend=False
    ))

# Update layout
fig.update_layout(
    scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=1)),
    margin=dict(l=10, r=10, b=0, t=15),
    legend=dict(x=0.95, y=0.4, traceorder="normal", font=dict(family="sans-serif", size=12, color="black"),
                tracegroupgap=15),
    # width=800,
    # height=300
)










# Calculate 95% of the original width and height
new_width = int(0.9 * 600)
new_height = int(0.9 * 450)

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
    
        # Create a QHBoxLayout and add the widgets
        layout = QHBoxLayout()
        layout.addWidget(self.browser)
        # Add Another central_widget
        #layout.addWidget(self.obj_widget)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

# Run the PyQt5 application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())