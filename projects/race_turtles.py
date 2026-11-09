# MM, 1st period Programming I, Turtle Race

import turtle as t
import random as r
import time

def race(condition, listed):
    for turtle in listed:
        turtle.fd(r.randint(0,50))
        if turtle.xcor() >= 550:
            condition = turtle
            break
    return condition

finish_line = t.Turtle()
finish_line.hideturtle()

# C:U turtles in honor of the game releasing on the 9th (today, as of writing)
gray_turtle = t.Turtle() # Expie
gray_turtle.color("#928F87")

blue_turtle = t.Turtle() # Milky
blue_turtle.color("#93F8F0")

yellow_turtle = t.Turtle() # Dune
yellow_turtle.color("#FFC375")

pink_turtle = t.Turtle() # Observer (I literally cannot think of anybody else)
pink_turtle.color("#E452A2")

brown_turtle = t.Turtle() # Moffee?
brown_turtle.color("#A55036")

t.bgcolor("#241B1B")
lineup = [gray_turtle,  blue_turtle, pink_turtle, yellow_turtle, brown_turtle]
names = ["Expie (Gray)", "Milky (Blue)", "Observer (Pink)", "Dune (Yellow?)", "Moffee (Brown)"]


for turtle in lineup:
    turtle.showturtle()

y = -150
for turtle in lineup:
    turtle.teleport(-550, y )
    y += 100

finish_line.color("red")
finish_line.speed(100)
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