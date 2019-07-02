import turtle
import random

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def drawArray(arr, left, right, pivot, colFront = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(len(arr)):
        t.sety(-height / 2)
        if i == left or i == right:
            t.fillcolor("red")
        elif i == pivot:
            t.fillcolor("#00D51F")
        elif i < left:
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

def organize(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        drawArray(arr, i, j, pivot) 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        a = organize(arr, low, high)
        quickSort(arr, low, a - 1)
        quickSort(arr, a + 1, high)


def randomize(arr):
    random.shuffle(arr)
    return arr

arr = randomize([i for i in range(1, 101)])
quickSort(arr, 0, len(arr) - 1)
for i in range(len(arr) + 1):
    drawArray(arr, i, -1, -1, "#00D51F")
turtle.exitonclick()
turtle.mainloop()
