import turtle

turtle.shape("circle")
turtle.shapesize(0.5)
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(5)

turtle.penup()
turtle.goto(160, -180 )
turtle.pendown()

turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

turtle.left(90)
turtle.forward(100)

for i in range(20): 
    turtle.forward(7)
    turtle.left(3)
for i in range(20):
    turtle.forward(6)
    turtle.left(2)
    
turtle.done()