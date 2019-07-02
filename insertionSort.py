import turtle
import time
import random

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def drawArray(arr, count, indexAt, col, col2, colFront = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(len(arr)):
        t.sety(-height / 2)
        if i == indexAt:
            t.fillcolor(col2)
        elif abs(i - count) < 2 and i < indexAt:
            t.fillcolor(col)
        elif i < count:
            t.fillcolor(colFront)
        else:
            t.fillcolor("white")
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

def insertionSort(arr):
    drawArray(arr, 0, 0, "red", "black")
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            drawArray(arr, j, i, "red", "#00D51F")
    for i in range(len(arr) + 2):
        drawArray(arr, i, -1, "red", "black", "#00D51F")

def randomize(arr):
    random.shuffle(arr)
    return arr

insertionSort(randomize([i for i in range(1, 51)]))
turtle.exitonclick()
turtle.mainloop()

