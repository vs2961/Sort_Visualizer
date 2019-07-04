import turtle
import random

t = turtle.Turtle()
turtle.hideturtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)
turtle.bgcolor("black")

def drawArray(arr, left, right, colFront = "white"):
    t.clear()
    width = turtle.window_width()
    height = turtle.window_height()
    t.pu()
    height_constant = height / max(arr) 
    t.goto(-width / 2, -height / 2)
    for i in range(len(arr)):
        if i == left or i == right:
            t.fillcolor("red")
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

def merge(arr, low, high, mid): 
    left = list(arr[low:mid])
    right = list(arr[mid:high])
    ind1 = ind2 = 0
    replace = low
    while ind1 < len(left) and ind2 < len(right):
        drawArray(arr, low + ind1, mid + ind2) 
        if (left[ind1] < right[ind2]):
            arr[replace] = left[ind1]
            ind1 += 1
        else:
            arr[replace] = right[ind2]
            ind2 += 1
        replace += 1
    while ind1 < len(left):
        drawArray(arr, low + ind1, mid + ind2)
        arr[replace] = left[ind1]
        ind1 += 1
        replace += 1
    while ind2 < len(right):
        drawArray(arr, low + ind1, mid + ind2)
        arr[replace] = right[ind2]
        ind2 += 1
        replace += 1

def mergeSort(arr, low, high):
    mid = (low + high) // 2
    if len(arr[low:high]) > 1:
        mergeSort(arr, low, mid)
        mergeSort(arr, mid, high)
        a = merge(arr, low, high, mid)

def randomize(arr):
    random.shuffle(arr)
    return arr

arr = randomize([i for i in range(1, 101)])
mergeSort(arr, 0, len(arr))
for i in range(len(arr) + 1):
    drawArray(arr, i, -1, "#00D51F")
turtle.exitonclick()
turtle.mainloop()
