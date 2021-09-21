from turtle import Turtle, Screen

# import turtle
# tim = turtle.Turtle()
# OR
# import turtle as t
# tim = t.Turtle()

# 7. Spirograph
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim.speed('fastest')
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)
draw_spirograph(5)

# 6.Random walk with random colors RGB by Tuple
# tuple = (1,2,8) - has ordered items
# tuple[2] - gives 8
# tuple[2] = 12 - it does not change 8 to 12 like list i.e A Tuple is immutable , it cannot be changed
# list(tuple) - gives [1,2,8] -it convert Tuple into list

# color is defined by Tuple (r, g, b)

# import turtle as t
# import random
# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# direction = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed('fastest')
# for i in range(1000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# 5.Random walk limited colors
# import random
# tim = Turtle()
# colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]
# for i in range(200):
#     tim.forward(30)
#     tim.pensize(15)
#     tim.speed('fastest')
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(direction))

#4.Draw different colored shapes
# import random
# tim = Turtle()
# colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(sides):
#     angle = 360 / sides
#     for i in range(sides):
#         tim.forward(100)
#         tim.left(angle)
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

# OR
# 3.
# tim = Turtle()
# for i in range(3):
#     tim.pencolor('green')
#     tim.forward(100)
#     tim.left(120)
# for i in range(4):
#     tim.pencolor('blue')
#     tim.forward(100)
#     tim.left(90)
# for i in range(5):
#     tim.pencolor('yellow')
#     tim.forward(100)
#     tim.left(72)
# for i in range(6):
#     tim.pencolor('red')
#     tim.forward(100)
#     tim.left(60)
# for i in range(7):
#     tim.pencolor('brown')
#     tim.forward(100)
#     tim.left(51.4)
# for i in range(8):
#     tim.pencolor('coral')
#     tim.forward(100)
#     tim.left(45)
# for i in range(9):
#     tim.pencolor('cyan')
#     tim.forward(100)
#     tim.left(40)
# for i in range(10):
#     tim.forward(100)
#     tim.left(36)
# 2.Dotted line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# 1.square
# tim = Turtle()
# tom = Turtle()
# # terry = Turtle()
# tim.shape('turtle')
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)


screen = Screen()
screen.exitonclick()