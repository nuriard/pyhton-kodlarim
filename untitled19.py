import cv2
import turtle
from PIL import Image
import numpy as np

# --- AYARLAR ---
IMAGE_PATH = 'cmylmz.png.png'  
TURTLE_SPEED = 0
LINE_THICKNESS = 2
SCALE_FACTOR = 2
# -----------------

pil_img = Image.open(IMAGE_PATH).convert('L')
img_orig = np.array(pil_img)
height, width = img_orig.shape
new_size = (int(width * SCALE_FACTOR), int(height * SCALE_FACTOR))

pil_resized = pil_img.resize(new_size, Image.BOX)
img = np.array(pil_resized)

edges = cv2.Canny(img, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

screen = turtle.Screen()
screen.title("Turtle Drawing")
screen.bgcolor("white")
screen.setup(width=new_size[0] + 100, height=new_size[1] + 100)
screen.setworldcoordinates(-50, new_size[1] + 50, new_size[0] + 50, -50)

t = turtle.Turtle()
t.hideturtle()
t.speed(TURTLE_SPEED)
t.pensize(LINE_THICKNESS)
t.color("black")

for contour in contours:
    first_point = True
    for point in contour:
        x, y = point[0]
        if first_point:
            t.penup()
            t.goto(x, y)
            t.pendown()
            first_point = False
        else:
            t.goto(x, y)

turtle.done()