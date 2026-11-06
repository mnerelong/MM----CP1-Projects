# MM, Period 1 Programming I, Libraries Notes

# -------------- alternate ways to type "import turtle"
import turtle as t #<-- so i only have to write 't' to use turtle.
#from turtle import *
# --------------

#docs.python.org
#^^^^^^^^^^^^^^^ official documentation site

t.showturtle()
t.speed(50)
# t.hideturtle() HIDE the turtle.

colors = ["green", "blue"]
t.fillcolor('white')
t.bgcolor('black')

# changes the shape of the 'turtle'
t.shape("square")
#stretches it out
t.shapesize(2, 1, 2)
t.shearfactor(12)

x=1
while True:
    for color in colors:
        t.color(color)
        t.forward(50)
        t.left((11%x)*10)
        x+=1

    if x > 100:
        break

t.clear()
print(f"Coordinates: {t.pos()}\nX: {t.xcor()}\nY: {t.ycor()}")

t.up() # lifts the pen and stops drawing.
t.goto(4,11)

print(f"Coordinates: {t.pos()}\nX: {t.xcor()}\nY: {t.ycor()}")
t.home()
t.exitonclick() # makes it so that the program only ends when you click on it
