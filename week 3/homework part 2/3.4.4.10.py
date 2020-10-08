import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.pensize(7)

for element in range(5):
    leonardo.forward(150)
    leonardo.right(144)

paper.exitonclick()