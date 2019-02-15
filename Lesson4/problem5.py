from turtle import *

yaya = Turtle()

yaya.color('orange')
yaya.pensize()
yaya.speed(3)
yaya.shape('turtle')

def drawHexagon():
	for x in range(6):
		yaya.forward(30)
		yaya.left(60)

for x in range(12):
	drawHexagon()
	yaya.left(30)

	

mainloop()