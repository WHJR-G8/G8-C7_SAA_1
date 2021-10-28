import turtle

n = int(input('Enter the value for number of sides of polygon: '))
side = int(input('Enter the length of side of polygon: '))
color1 = input('Enter the color polygon 1: ')
color2 = input('Enter the color polygon 2: ')

def draw_polygon():
    for variable in range(0, n):
        turtle.forward(side)
        turtle.right(360 / n)
        
turtle.pencolor(color1)
draw_polygon()

turtle.penup()
turtle.goto(80, 40)
turtle.pendown()

turtle.pencolor(color2)
draw_polygon()
