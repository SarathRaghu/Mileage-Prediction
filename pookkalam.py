import turtle
t=turtle.Turtle()
s=100
for i in range(6):
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.left(60)
    t.circle(100)
turtle.mainloop()