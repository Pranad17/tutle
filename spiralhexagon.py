import turtle
hex = turtle.Pen()
colors = ["cyan", "purple","blue","green","orange","yellow"]
turtle.bgcolor("black")
for i in range(360):
    hex.pencolor(colors[i % 6])
    hex.width(i/100+1)
    hex.forward(100)
    hex.left(60)