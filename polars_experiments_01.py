import numpy as np
import polars as pl
import plotly.graph_objects as go


def generate_square_coordinates(side_length):
    """
    Generate coordinates for a square with a given side length.
    
    Parameters:
    side_length (int or float): The length of each side of the square.
    
    Returns:
    np.ndarray: A 2D array of shape (5, 2) representing the coordinates of the square.
    """
    # Define the four corners of the square
    corners = np.array([
        [0, 0],                  # Bottom-left corner
        [side_length, 0],        # Bottom-right corner
        [side_length, side_length], # Top-right corner
        [0, side_length],        # Top-left corner
        [0, 0]                   # Closing the square by returning to the bottom-left corner
    ])
    return corners

# Example usage
side_length = 5
square_coordinates = generate_square_coordinates(side_length)
print(square_coordinates)

# # Square Plot
# # Create a Plotly line plot
# fig = go.Figure()
# # Add the square as a line plot
# fig.add_trace(go.Scatter(
#     x=square_coordinates[:, 0],
#     y=square_coordinates[:, 1],
#     mode='lines+markers',
#     name='Square'
# ))
# # Set plot title and labels
# fig.update_layout(
#     title='Square Line Plot',
#     xaxis_title='X',
#     yaxis_title='Y',
#     xaxis=dict(scaleanchor="y", scaleratio=1),  # Ensuring square aspect ratio
#     yaxis=dict(scaleanchor="x", scaleratio=1)   # Ensuring square aspect ratio
# )
# # Show the plot
# fig.show()

print()
# Convert the NumPy array to a Polars DataFrame
df = pl.DataFrame({
    "x": square_coordinates[:, 0],
    "y": square_coordinates[:, 1]
})
print(df)
