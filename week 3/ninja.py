import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
leonardo.pensize(7)

for element in range(5):
    leonardo.color(colors[element % len(colors)])
    leonardo.forward(150)
    leonardo.right(144)

paper.exitonclick()
