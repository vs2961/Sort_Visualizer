import turtle
import random
import math

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def decideColor(count):
    cols = ["purple", "blue", "green", "orange", "red", "brown"]
    return cols[int(math.log(count, 2)) % 6]

def drawArray(arr, count, coloring, colFront = "white", colBack = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(1, len(arr) + 1):
        if colFront != "white" and i <= count:
            t.fillcolor(colFront)
        elif (i >= count and coloring) or (i <= count and not coloring):
            t.fillcolor(decideColor(i))
        else:
            t.fillcolor(colBack)
        t.setheading(90)
        t.pd()
        t.begin_fill()
        t.fd(arr[i - 1] * height_constant)
        t.rt(90)
        t.fd(width / len(arr))
        t.rt(90)
        t.fd(arr[i - 1] * height_constant)
        t.rt(90)
        t.fd(width / len(arr))
        t.rt(180)
        t.fd(width / len(arr))
        t.end_fill()
    turtle.update()

def heapify(arr, n, i, coloring, colorCount = 0): 
    drawArray(arr, colorCount if coloring else n, coloring)
    x = i
    right = 2 * i + 2
    left = 2 * i + 1
    if left < n and arr[i] < arr[left]:
        x = left
    if right < n and arr[x] < arr[right]:
        x = right
    if x != i:
        arr[i], arr[x] = arr[x], arr[i]
        heapify(arr, n, x, coloring, colorCount)

def heapSort(arr):
    a = len(arr)
    for i in range(a, -1, -1):
        heapify(arr, a, i, True, i)

    for i in range(a - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, False)
        

def randomize(arr):
    random.shuffle(arr)
    return arr

arr = [i for i in range(1, 128)]
heapSort(randomize(arr))
for i in range(len(arr) + 1):
    drawArray(arr, i, False, colFront = "#00D51F")
turtle.exitonclick()
turtle.mainloop()
