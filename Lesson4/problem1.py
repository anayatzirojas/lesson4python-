from turtle import *

yaya = Turtle()

yaya.color('orange')
yaya.pensize(5)
yaya.speed(8)
yaya.shape('turtle')
yaya.turtlesize(5,5,5)

for x in range(4):
	yaya.forward(80)
	yaya.left(50)
	yaya.forward(200)
	yaya.right(150)
	yaya.forward(50)
	yaya.circle(25)
	yaya.backward(30)
	yaya.circle(50)

mainloop()
