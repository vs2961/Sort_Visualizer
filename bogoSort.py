import turtle
import random

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def drawArray(arr, count, colFront = "white", colBack = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(len(arr)):
        if i < count:
            t.fillcolor(colFront)
        else:
            t.fillcolor(colBack)
        t.setheading(90)
        t.pd()
        t.begin_fill()
        t.fd(arr[i] * height_constant)
        t.rt(90)
        t.fd(width / len(arr))
        t.rt(90)
        t.fd(arr[i] * height_constant)
        t.rt(90)
        t.fd(width / len(arr))
        t.rt(180)
        t.fd(width / len(arr))
        t.end_fill()
    turtle.update()

def bogoSort(arr):
    while True:
        drawArray(arr, -1)
        ordered = True
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                ordered = False
        if ordered:
            break
        randomize(arr)
    for i in range(len(arr) + 1):
        drawArray(arr, i, "#00D51F")

def randomize(arr):
    random.shuffle(arr)
    return arr

bogoSort(randomize([i for i in range(1, 11)]))
turtle.exitonclick()
turtle.mainloop()
