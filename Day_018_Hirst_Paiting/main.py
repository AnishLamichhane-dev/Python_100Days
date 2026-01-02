# import colorgram
# colors = colorgram.extract('painting.jpg',30)
# total_colors = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     total_colors.append((r,g,b))
# print(total_colors)

import turtle

colors_list = [ (232, 157, 72), (39, 116, 156), (217, 174, 10), (163, 57, 73), (109, 165, 196),
 (244, 203, 80), (49, 131, 73), (217, 82, 65), (127, 187, 145), (208, 227, 218),
 (199, 67, 81), (211, 130, 143), (140, 64, 58), (23, 91, 70), (49, 154, 184),
 (74, 164, 135), (236, 160, 184), (68, 49, 47), (104, 47, 60), (96, 52, 50), (233, 174, 162), (68, 48, 49),
 (169, 206, 173), (48, 66, 60), (159, 203, 215), (118, 118, 155), (246, 195, 5),
                ]

turtle.hideturtle()
turtle.colormode(255)
turtle.speed('fastest')
turtle.setheading(225)
turtle.penup()
turtle.forward(250)
turtle.setheading(0)
a=0
b=0

for each_row in range(10):
    b+=50
    turtle.teleport(-220, -280 + b)
    for each_column in range(10):
        if a >= len(colors_list):
            a = 0
        turtle.dot(20, colors_list[a])
        turtle.penup()
        turtle.forward(50)
        a += 1

screen = turtle.Screen()
screen.exitonclick()