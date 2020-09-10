import turtle as t

x=0
y=0

while(y<600):
    t.forward(500)
    y+=100
    t.penup()
    t.goto(x,y)
    t.pendown()
y=0

t.penup()
t.goto(x,y)
t.pendown()

t.left(90)
while(x<600):
    t.forward(500)
    x+=100
    t.penup()
    t.goto(x,y)
    t.pendown()

t.exitonclick()
