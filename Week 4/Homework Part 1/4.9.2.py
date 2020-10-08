import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.color("hotpink")

def square(leonardo, size):
    for _ in range (4):
        leonardo.forward(size)
        leonardo.left(90)

    leonardo.penup()
    leonardo.left(-90)
    leonardo.forward(10)
    leonardo.left(90)
    leonardo.forward(-10)
    leonardo.pendown()

for n in range (1,6):
    square(leonardo, n*20)

paper.exitonclick()
