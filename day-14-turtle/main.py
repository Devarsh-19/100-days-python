from re import S
from secrets import choice
from turtle import *
from random import randint
import turtle


tim = Turtle()

# tim.shape("turtle")
# tim.color("red")

# #RECTANGLE

# for x in range(4):
#     tim.forward(100)
#     tim.left(90)

# ----------------------------------------------------------------------------


# #DASHED LINE

# for x in range(20):
#     tim.forward(5)
#     tim.pu()
#     tim.forward(5)
#     tim.pd()
# ------------------------------------------------------

# # SHAPES

# tim.hideturtle()

# colors = ["red", "orange", "pink", "black", "blue", "cyan", "green"]

# s = 3

# for i in range(9):
#     tim.color(choice(colors))
#     for y in range(s):
#         tim.forward(100)
#         tim.left(360/s)
        
#     s +=1



# -------------------------------------------------

# # RANDOM WALK

# tim.hideturtle()
# colors = ["red", "orange", "pink", "black", "blue", "cyan", "green", "brown", "purple"]
# tim.pensize(width=4)
# tim.speed(0)

# direction = [0 , 90, 180, 270]

# for i in range(200):
#     tim.forward(30)
#     tim.setheading(choice(direction))
#     tim.color(choice(colors))


# -------------------------------------------------
def gen_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tp = (r, g,b)
    return tp
    
# turtle.bgcolor("black")
# tim.hideturtle()
# colors = ["red", "orange", "pink", "black", "blue", "cyan", "green", "brown", "purple"]
# tim.pensize(width=8)
# tim.speed("fastest")
# turtle.colormode(255)

# direction = [0 , 90, 180, 270]

# for i in range(200):
#     tim.forward(30)
#     tim.setheading(choice(direction))
#     tim.color(gen_color())

#---------------------------------------------------------------------------------------------------------------------

# SPIROGRAPH

# turtle.bgcolor("black")

# tim.hideturtle()
# tim.pensize(width=2)
# tim.speed("fastest")
# turtle.colormode(255)

# for i in range(150):
#     tim.circle(90)
#     tim.setheading(tim.heading()+5)
#     tim.color(gen_color())

# screen = turtle.Screen()

# exitonclick()


# import colorgram

# turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('day-14-turtle\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
    
# tim.pu()
# tim.setheading(-150)
# tim.fd(300)
# tim.setheading(0)


# for i in range(1,101):
#     tim.fd(50)
#     tim.pd()
#     tim.dot(20,choice(rgb_colors))
#     tim.pu()
#     if i % 10 == 0:
#         tim.setheading(90)
#         tim.fd(50)
#         tim.setheading(180)
#         tim.fd(500)
#         tim.setheading(0)
    
# screen = turtle.Screen()
# exitonclick()


