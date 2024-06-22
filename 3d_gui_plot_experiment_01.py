import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from threading import Thread
import time

# Function to run the Dash app
def run_dash():
    app.run_server()

# Create a Dash application
app = dash.Dash(__name__)
fig = go.Figure(data=[go.Scatter3d(
    x=[1, 2, 3, 4, 5],
    y=[5, 6, 7, 8, 9],
    z=[10, 11, 12, 13, 14],
    mode='markers'
)])
app.layout = html.Div([
    dcc.Graph(figure=fig)
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
        self.setGeometry(100, 100, 800, 600)

        # Create a QWebEngineView and set the Dash app URL
        self.browser = QWebEngineView()
        self.browser.setUrl("http://127.0.0.1:8050")

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