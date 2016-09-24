import twilio
import turtle

print(twilio.__version__)

'''
def Rhombus(brad):
	for i in range(1,3):
		brad.left(45)
		brad.forward(200)
		brad.left(135)
		brad.forward(200)

window = turtle.Screen()
brad = turtle.Turtle()
brad.speed(10)

for i in range(0, 36):
	Rhombus(brad)
	brad.right(10)

window.exitonclick()

import turtle

def Triangle(brad, x):
	for i in range(0, 2):
		brad.forward(x)
		brad.left(120)
	brad.forward(x)
	brad.right(0)
	brad.backward(x/2)
	x = x/2
	InverseTriangleBackward(brad, x)
	x = x/2
	InverseTriangleForward(brad, x)
	x = x/2
	brad.right(180)
	InverseTriangleForward(brad, x)

def InverseTriangleBackward(brad, x):
	brad.right(60)
	for i in range(0, 3):
		brad.backward(x)
		brad.right(120)

def InverseTriangleForward(brad, x):
	brad.right(120)
	brad.forward(x)
	brad.right(60)
	for i in range(0, 3):
		brad.forward(x)
		brad.right(120)

def customShape():
	window = turtle.Screen()
	brad = turtle.Turtle()
	Triangle(brad, 200);
	
customShape()
'''