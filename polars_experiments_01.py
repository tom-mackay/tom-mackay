import numpy as np
import polars as pl


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

# Install plotly 