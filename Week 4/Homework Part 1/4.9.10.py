import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()


def draw_star(drawing_leonardo):
    for _ in range(5):
        drawing_leonardo.forward(100)
        drawing_leonardo.right(144)

for _ in range (5):
    draw_star(leonardo)
    leonardo.penup()
    leonardo.forward(350)
    leonardo.right(144)
    leonardo.pendown()


paper.exitonclick()