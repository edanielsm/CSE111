import tkinter as tk
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    draw_sky(canvas)
    draw_ground(canvas)
    draw_clouds(canvas)
    draw_ceiling(canvas)
    draw_wall(canvas)
    draw_door(canvas)
    draw_windows(canvas)
    draw_trunk(canvas)
    draw_pine(canvas)
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    #tree_center = scene_left + 500
    #tree_top = scene_top + 100
    #tree_height = 150
    #draw_pine_tree(canvas, tree_center, tree_top, tree_height)

def draw_sky(canvas):
    canvas.create_rectangle(0,0,799, 325, fill = '#30B3F8')

def draw_ground(canvas):
    canvas.create_rectangle(0,325,799, 599, fill = "#1BB93A")

def draw_clouds(canvas):
    canvas.create_oval(20,20,150,80, fill = '#FFFFFF', outline = '#FFFFFF')
    canvas.create_oval(35,35,190,120, fill = '#FFFFFF', outline = '#FFFFFF')
    canvas.create_oval(110,20,225,100, fill = '#FFFFFF', outline = '#FFFFFF')
    canvas.create_oval(200,20,450,80, fill = '#FFFFFF', outline = '#FFFFFF')
    canvas.create_oval(235,35,510,120, fill = '#FFFFFF', outline = '#FFFFFF')
    canvas.create_oval(350,20,650,100, fill = '#FFFFFF', outline = '#FFFFFF')

def draw_ceiling(canvas):
    canvas.create_polygon(550,150, 450,250, 650, 250, fill = '#3D260C')

def draw_wall(canvas):
    canvas.create_rectangle(475,250,625,400, fill= '#F56E6E')

def draw_door(canvas):
    canvas.create_rectangle(500,325,550,400, fill= 'blue')

def draw_windows(canvas):
    canvas.create_rectangle(560,265,580,280, fill= 'yellow')
    canvas.create_rectangle(580,265,600,280, fill= 'yellow')
    canvas.create_rectangle(560,280,580,295, fill= 'yellow')
    canvas.create_rectangle(580,280,600,295, fill= 'yellow')

def draw_trunk(canvas):
    canvas.create_rectangle(125,275,160,400, fill = '#6D3003')

def draw_pine(canvas):
    canvas.create_polygon(150,50, 50,290, 250,290, fill = '#1C6702')




    #for x in range(0,10):
        #canvas.create_(random.randint(0,250), random.randint(0,150), random.randint(0,250), random.randint(0,150), fill = "#FFFFFF")



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


# def draw_pine_tree(canvas, peak_x, peak_y, height):
#     """Draw a single pine tree.
#     Parameters
#         canvas: The tkinter canvas where this
#             function will draw a pine tree.
#         peak_x, peak_y: The x and y location in pixels where
#             this function will draw the top peak of a pine tree.
#         height: The height in pixels of the pine tree that
#             this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = peak_x - trunk_width / 2
#     trunk_right = peak_x + trunk_width / 2
#     trunk_bottom = peak_y + height

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = peak_x - skirt_width / 2
#     skirt_right = peak_x + skirt_width / 2
#     skirt_bottom = peak_y + skirt_height

#     # Draw the trunk of the pine tree.
#     canvas.create_rectangle(trunk_left, skirt_bottom,
#             trunk_right, trunk_bottom,
#             outline="gray20", width=1, fill="tan3")

#     # Draw the crown (also called skirt) of the pine tree.
#     canvas.create_polygon(peak_x, peak_y,
#             skirt_right, skirt_bottom,
#             skirt_left, skirt_bottom,
#             outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()