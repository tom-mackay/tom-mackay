from ursina import *
from direct.actor.Actor import Actor
from math import atan2, pi

#? Map Class Entity
class runeworld_map(Entity):
    def __init__(self):
            # Load a low-poly ground texture
            low_poly_texture = load_texture('textures/basic_grass.png')
            # Create the first ground entity using the built-in plane model
            ground = Entity(
                model='plane', 
                texture=low_poly_texture, 
                scale=(100, 1, 100),  # Extend the scale along the x-axis to connect with the second entity
                position=(0, 0, 0)
            )
            # Create a MeshCollider for the ground entity
            ground.collider = 'mesh'
            ground.collider_info = MeshCollider(entity=ground, mesh='quad')

#* Character Class Entity
class main_character(Entity):
    def __init__(self):
        super().__init__()
        # Character Model and Animation Paths
        model_path = 'animations/BASEmodel.glb'
        character = Entity(scale=(2, 3, 2))
        # Load the actor for the character animation
        actor = Actor(model_path)
        actor.reparentTo(character) # 2 Animations Currently for Idle and Walk
        # Speed at which the character moves towards target positions
        move_speed = 0.0125
        
    def correct_lookat(entity):
        entity.rotation_y += 180  # Rotate 180 degrees
        
        
        
        
        
        
        
        
          
        
if __name__ == '__main__':

    def distance(a, b):
        return (a - b).length()

    runeworld = Ursina()
    runeworld_map()
    main_character()

    # Variable to keep track of the previous mouse state
    prev_mouse_state = False #! Default Position 
    target_position = None
    is_moving = False

def update():
    global prev_mouse_state, is_moving, target_position
    if mouse.left and not prev_mouse_state:
        if mouse.hovered_entity == runeworld_map.ground:
            print("Moving character to:", mouse.world_point)
            target_position = mouse.world_point
            main_character.character.look_at(main_character.target_position)  # Rotate the character to face the target position
            # Determine the direction the character is moving in
            movement_direction = mouse.world_point - main_character.character.position
            movement_direction.y = 0  # Ensure the character stays on the ground

            # Calculate the target position based on the movement direction
            main_character.target_position = main_character.character.position + movement_direction

            main_character.correct_lookat(main_character.character)  # Make the character look away
            main_character.is_moving = True
            main_character.actor.loop('standard_walk')
        prev_mouse_state = True  # Set to True only when a new click is detected

    if main_character.is_moving:
        main_character.character.position = lerp(main_character.character.position, target_position, main_character.move_speed)
        if distance(main_character.character.position, target_position) < 3.0:  # Check if the character is close enough to the target
            target_position = None
            prev_mouse_state = False  # Reset prev_mouse_state after the character has reached the target position
            is_moving = False
            
        else:
            if not main_character.actor.getCurrentAnim():  # Start the animation if it is not currently playing
                main_character.actor.stop('standing_idle')
                main_character.actor.loop('standard_walk')
    else:
        #actor.stop('standard_walk') 
        main_character.actor.loop('standing_idle')
        None
    prev_mouse_state = mouse.left







# Add an editor camera for better control
EditorCamera()
# Add lighting
DirectionalLight(parent=scene, y=2, z=3, shadows=True)
AmbientLight(color=color.rgba(100, 100, 100, 0.5))
runeworld.run()