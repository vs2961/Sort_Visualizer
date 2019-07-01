import turtle
import time
import random

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def drawArray(arr, count, col, colFront = "white", colBack = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(len(arr)):
        if i == count:
            t.fillcolor(col)
        elif i < count:
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

def selectionSort(arr):
    for i in range(len(arr)):
        least = i
        for j in range(len(arr) - i):
            drawArray(arr, i + j, "red")
            if arr[j + i] < arr[least]:
                least = j + i
        arr[i], arr[least] = arr[least], arr[i]
    for i in range(len(arr) + 1):
        drawArray(arr, i , "red", "#00D51F")

def randomize(arr):
    random.shuffle(arr)
    return arr

selectionSort(randomize([i for i in range(51)]))
turtle.exitonclick()
turtle.mainloop()

