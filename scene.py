import bpy
import random
import pickle
#------------------------------------------------
#print("hi")
# bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
# bpy.ops.mesh.primitive_cube_add( size=1, location=(0,0,0))
# print(dir(bpy.data.objects["Car"]))
# print(dir(bpy.data.textures.get("body")))
# bpy.data.materials["Body"].diffuse_color[0, 0.00289276, 1, 1]
#------------------------------------------------

#Global vars
active_object = bpy.context.view_layer.objects.active 
Car = bpy.data.objects["Car"]
Plate_text = bpy.data.objects["plate_text"]
Car_body_mat = bpy.data.materials["Body"]
train_before = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\Train\Before"
train_after = r"C:\Users\monac\Documents\GitHub\DeepForSpeed\Dataset\Train\After"
train_speed_txt = r".\Dataset\Train\speed.txt"
license_plate_list = ["MH 1010", "BX 2050", "KP 3001", "PX 8029", "GM 8980"]
car_colour_list = [
    [1, 0, 0, 1], 
    [1, 1, 1, 1], 
    [1, 1, 0, 1], 
    [0, 0.5, 1, 1], 
    [0, 1, 0, 1]] #RED, White, Yellow, blue, green
count = 0
speed_list = []
plate_list = []

#Fns
# def select_car():
#     bpy.ops.object.select_all(action='DESELECT')
#     active_object = Car
#     Car.select_set(True)

# def move_car(dist = 1):
#     select_car()
#     # bpy.ops.transform.translate(value = (0, dist, 0))
#     bpy.context.object.location[1] = 3

def speed_to_dist(speed):
    # mov = "movement in meters in 0.25s:"
    return round((speed*1000)/(60*60*4),5)

def init_pos():
    return round(random.uniform(3,5),5)

#Execs

Plate_text.data.body = random.choice(license_plate_list)
Car_body_mat.diffuse_color[random.choice(car_colour_list)]

# speed = random.randint(0,150)
# speed_list.append(speed)
# Car.location.y = init_pos()
# bpy.context.scene.render.filepath = f"{train_before}\{count}.jpg"
# bpy.ops.render.render(write_still = True)

# Car.location.y += speed_to_dist(speed)
# bpy.context.scene.render.filepath = f"{train_after}\{count}.jpg"
# bpy.ops.render.render(write_still = True)

# with open(train_speed_txt, "wb") as fp:
#     pickle.dump(speed_list, fp)
