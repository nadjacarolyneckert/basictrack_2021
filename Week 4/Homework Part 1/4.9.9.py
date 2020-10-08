import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()


def draw_star(drawing_leonardo):
    for _ in range(5):
        drawing_leonardo.forward(150)
        drawing_leonardo.right(144)

draw_star(leonardo)

paper.exitonclick()
