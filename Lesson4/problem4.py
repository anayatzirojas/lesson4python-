from turtle import *

yaya = Turtle()

yaya.color('orange')
yaya.pensize(4)
yaya.speed(4)
yaya.shape('turtle')

kawtar = Turtle()

kawtar.color('red')
kawtar.pensize(4)
kawtar.speed(4)
kawtar.shape('turtle')

for x in range(3):
	yaya.forward(60)
	yaya.left(120)

kawtar.circle(100)


mainloop()