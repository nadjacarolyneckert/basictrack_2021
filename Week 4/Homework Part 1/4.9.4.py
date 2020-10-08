import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.color("pink")

def draw_poly(draw_turtle, number_of_sides, size):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        draw_turtle.forward(size)
        draw_turtle.left(angle)

for _ in range(20):
    draw_poly(leonardo, 4, 150)
    leonardo.left(360 / 20)

paper.exitonclick()
