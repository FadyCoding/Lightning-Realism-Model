import bpy
import random

def look_at(obj, target):
    direction = target.location - obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

def set_camera_position(camera, x, y, z):
    camera.location.x = x
    camera.location.y = y
    camera.location.z = z

camera = bpy.context.scene.camera
target_object = bpy.data.objects['BezierCircle']

# Set the number of images
num_images = 1000

for i in range(num_images):
    # Random position for camera
    x = random.uniform(-5, 5)  
    y = random.uniform(-5, 5)  
    z = random.uniform(2, 8)   

    set_camera_position(camera, x, y, z)
    look_at(camera, target_object)

    # Render and save the image
    bpy.context.scene.render.filepath = f'C:\\Users\\Fady\\Desktop\\IA_Project\\RenderedLightning\\image_{i}.png'
    bpy.ops.render.render(write_still=True)
