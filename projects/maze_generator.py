# MM , period 1 Programming I, Maze Generator

import turtle as t
import random as r


t.teleport(-360, 360)
t.color('white')
t.bgcolor('black')

rows = [[],[],[],[],[],[]]
columns = [[],[],[],[],[],[]]

sub = 0
for i in range(6):
    for x in range(6):
        columns[sub].append(r.randint(0,1))
        rows[sub].append(r.randint(0,1))
    sub += 1
    

print(rows)
print(columns)

for row in rows:
    for space in row:
        if space:
            t.pendown()
            t.forward(60)
        else:
            t.penup()
            t.forward(60)
    t.teleport(-360, t.ycor() - 60)

t.teleport(-360, 360)
t.right(90)
for column in columns:
    for space in column:
        if space:
            t.pendown()
            t.forward(60)
        else:
            t.penup()
            t.forward(60)
    t.teleport(t.xcor() + 60, 360)

t.exitonclick()