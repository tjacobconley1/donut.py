import bpy
import math
import numpy as np
verticies = []


def rotation_matrix(axis, theta):
  """ 
  returns the rotation matrix associated with counterclockwise
  rotation about the given axis by theta radians 
  """
  axis =np.array(axis)
  axis = axis / math.sqrt(np.dot(axis, axis))
  a = math.cos(theta/2.0)
  b, c, d = -axis * math.sin(theta/2.0)
  aa, bb, cc, dd = a*a, b*b, c*c, d*d
  bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
  return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                   [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                   [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

def circle(radius, location):
    circle_verticies = []
    (a, b, c) = location
    for angle in range(0, 360, 10):
        angle_radius = math.radians(angle)
        x = a + radius * math.cos(angle_radius)
        y = b + radius * math.sin(angle_radius)
        circle_verticies.append((x, y, c))
    # adding first verticie as last element in order
    # to connect the last verticies to the start
    circle_verticies.append(circle_verticies[0])    
    return circle_verticies


total_height = 10
circle_radius = 3
row_height = 0.5

cylinder_verticies = []
per_circle_verticies = 0


circle_verticies = circle(circle_radius, (10,0,0))
per_circle_verticies = len(circle_verticies)
axis = (0,1,0)
delta_angle=10

sphere_verticies = []
for angle in range(0, 370, delta_angle):
    theta = math.radians(angle)
    circle_verticies_rotated = []
    for vertex in circle_verticies:
        vertex_rotated = np.dot(rotation_matrix(axis, theta), vertex)
        circle_verticies_rotated.append(vertex_rotated)
    
    sphere_verticies+=circle_verticies_rotated

donut_rows = int(370/ delta_angle)

faces = []

for row in range(0, donut_rows -1):
    for index in range(0, per_circle_verticies -1):
        vertex1 = index + (row * per_circle_verticies)
        vertex2 = vertex1 + 1
        vertex3 = vertex1 + per_circle_verticies
        vertex4 = vertex2 + per_circle_verticies
        face = (vertex1, vertex3, vertex4, vertex2)
        print(face)
        faces.append(face)

    
    
new_mesh = bpy.data.meshes.new("new_mesh")
new_mesh.from_pydata(sphere_verticies, [], faces)
new_mesh.update()

new_object = bpy.data.objects.new("donut", new_mesh)
view_layer = bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)


## CREATE ANIMATION 
donut = bpy.data.objects["donut"]

for angle in range(0, 360, 10):
    donut.rotation_euler = (math.radians(angle), math.radians(angle), math.radians(angle))
    donut.keyframe_insert(data_path="rotation_euler", frame=angle)
