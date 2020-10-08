import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

def draw_poly(draw_turtle, number_of_sides, size):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        draw_turtle.forward(size)
        draw_turtle.left(angle)


def draw_equitriangle(draw_turtle, size):
    draw_poly(draw_turtle, 3, size)

for _ in range (10):
    draw_equitriangle(leonardo, 100)
    leonardo.left(360/10)

paper.exitonclick()