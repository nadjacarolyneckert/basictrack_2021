
import turtle

pirate_moves = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

paper = turtle.Screen()
leonardo = turtle.Turtle()

for (angle, steps) in pirate_moves:
    leonardo.left(angle)
    leonardo.forward(steps)

paper.exitonclick()
