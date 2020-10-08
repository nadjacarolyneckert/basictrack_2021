import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.color("green")

leonardo.speed(0)

for step in range(100):
    leonardo.forward(step * 5)
    leonardo.right(89)

paper.exitonclick()
