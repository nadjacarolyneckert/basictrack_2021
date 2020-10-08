import turtle

paper = turtle.Screen()
tess = turtle.Turtle()

for _ in range(3):
    tess.forward(30)
    tess.left(120)

for _ in range(4):
    tess.forward(30)
    tess.left(90)

for _ in range(6):
    tess.forward(30)
    tess.left(60)

for _ in range(8):
    tess.forward(30)
    tess.left(45)

for _ in range(18):
    tess.forward(30)
    tess.left(360 / 18)

paper.exitonclick()