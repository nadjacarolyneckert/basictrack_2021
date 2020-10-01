import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']

for element in range(24):
    leonardo.color(colors[element % len(colors)])
    if element % 3 == 0:
        leonardo.forward(50)
    else:
        leonardo.forward(30)
    leonardo.right(15)

paper.exitonclick()
