import turtle
paper = turtle.Screen()
leonardo = turtle.Turtle()


def draw_poly(draw_turtle, number_of_sides, size):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        draw_turtle.forward(size)
        draw_turtle.left(angle)

draw_poly(leonardo, 8, 50)

paper.exitonclick()