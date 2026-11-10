# MM, 1st period Programming I, Turtle Race

import turtle as t
import random as r
import time

def turtle_color(turtles, colors):
    """This function colors each of the turtles accordingly."""
    for turtle in turtles:
        turtle.color(colors[(turtles.index(turtle))])
    return turtle

finish_line = t.Turtle()
finish_line.hideturtle()

# C:U turtles in honor of the game releasing on the 9th (today, as of writing)
gray_turtle = t.Turtle() # Expie

blue_turtle = t.Turtle() # Milky

yellow_turtle = t.Turtle() # Dune

pink_turtle = t.Turtle() # Observer (I literally cannot think of anybody else)

brown_turtle = t.Turtle() # Moffee?
# it's the 10th and moffee was livestreaming this morning... not playing C:U, however.

t.bgcolor("#241B1B")
lineup = [gray_turtle,  blue_turtle, pink_turtle, yellow_turtle, brown_turtle]
colors = ["#928F87", "#93F8F0", "#E452A2" ,"#FFC375", "#A55036"]
names = ["Expie (Gray)", "Milky (Blue)", "Observer (Pink)", "Dune (Yellow?)", "Moffee (Brown)"]

turtle_color(lineup, colors) # colors the turtles so that I don't have to do it manually.

for turtle in lineup:
    turtle.showturtle()
    turtle.shape("turtle"); turtle.shapesize(0.75)

y = -150
for turtle in lineup:
    turtle.teleport(-550, y )
    y += 100 # changes the y value by a set amount so that they're all a specific distance from each other.
#
finish_line.color("red") # finish line here
finish_line.speed(0)
finish_line.teleport(550, -500); finish_line.goto(550, 500)

for name in names:
    print(name)

win = 0

while win == 0:
    for turtle in lineup:
        turtle.fd(r.randint(0,50))
        if turtle.xcor() >= 550:
            win = turtle
            break

print(f"\n{names[lineup.index(win)]} has won!")
t.exitonclick()