from ursina import *
from math import isclose

app = Ursina()

# Load a low-poly texture
low_poly_texture = load_texture('textures/basic_grass.png')

# Create the first ground entity using the built-in plane model
ground1 = Entity(
    model='plane', 
    texture=low_poly_texture, 
    scale=(100, 1, 100),  # Extend the scale along the x-axis to connect with the second entity
    position=(0, 0, 0)
)

# Create a MeshCollider for the ground entity
ground1.collider = 'mesh'
ground1.collider_info = MeshCollider(entity=ground1, mesh='quad')

# Create a character entity
character = Entity(model='cube', color=color.orange, position=(0, 1, 0), scale=(2, 5, 2))  # Adjust the model and color as needed
# Create an entity to act as the camera
camera = Entity(parent=character, position=(0, 2, -5))  # Place the camera behind the character

# Speed at which the character moves towards the target position
move_speed = 0.02

# Variable to keep track of the previous mouse state
prev_mouse_state = False

# Target position for the character to move to
target_position = None

is_moving = False

def distance(a, b):
    return (a - b).length()

def update():
    global prev_mouse_state, is_moving, target_position
    if mouse.left and not prev_mouse_state:
        if mouse.hovered_entity == ground1:
            print("Moving character to:", mouse.world_point)
            target_position = mouse.world_point
            is_moving = True
        prev_mouse_state = True  # Set to True only when a new click is detected

    if is_moving:
        character.position = lerp(character.position, target_position, move_speed)
        if distance(character.position, target_position) < 0.1:  # Check if the character is close enough to the target
            target_position = None
            prev_mouse_state = False  # Reset prev_mouse_state after the character has reached the target position
            is_moving = False

    prev_mouse_state = mouse.left

    

# Add an editor camera for better control
EditorCamera()
# Add lighting
DirectionalLight(parent=scene, y=2, z=3, shadows=True)
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

app.run()