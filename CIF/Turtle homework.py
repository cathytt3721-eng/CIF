import turtle

turtle.color("blue")
turtle.shape("turtle")
turtle.speed(1)

sides=str(input("How many side do you want on your shape?"))
length=str(input("what length do you like your sides to be?"))
angle = (sides-2)*180/sides

for shape in range(sides):
    turtle.forward(length)
    turtle.left(180 - angle)

turtle.done()