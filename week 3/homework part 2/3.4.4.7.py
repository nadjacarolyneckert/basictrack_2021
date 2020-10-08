import turtle

paper = turtle.Screen()
pirate = turtle.Turtle()

pirate_steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for pirate_step in pirate_steps:
    pirate.forward(100)
    pirate.left(pirate_step)

print("Final heading of the pirate is", sum(pirate_steps) % 360)

paper.exitonclick()