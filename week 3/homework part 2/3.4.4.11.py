import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.shape("turtle")
leonardo.color("blue")

for element in range(12):

    leonardo.penup()
    leonardo.forward(100)
    leonardo.pendown()
    leonardo.forward(20)
    leonardo.penup()
    leonardo.forward(20)
    leonardo.stamp()
    leonardo.setposition(0,0)
    leonardo.right(360/12)

paper.exitonclick()