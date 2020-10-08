import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.color("hotpink")

def square(leonardo):
    for _ in range (4):
        leonardo.forward(20)
        leonardo.left(90)

    leonardo.penup()
    leonardo.forward(40)
    leonardo.pendown()

for _ in range(4):
    square(leonardo)

paper.exitonclick()