from turtle import Turtle,Screen

t=Turtle()
screen=Screen()
screen.setup(500,500)

screen.bgcolor("white")

t.penup()
t.goto(-160,-160)

t.color("black")
t.ondrag(t.goto)

t.pendown()
t.speed(5000)