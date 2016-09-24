import turtle

def Square(brad):
	for i in range(1,5):
		brad.forward(100)
		brad.right(90)

def Circle(brad):
	window = turtle.Screen()
#	brad = turtle.Turtle()
	brad.color("red")
	brad.circle(100)

def Triangle(brad):
	window = turtle.Screen()
#	brad = turtle.Turtle()
	brad.color("Green")
	for i in range(0,3):
		brad.forward(100)
		brad.left(120)

def Shapes():
	window = turtle.Screen()
	window.bgcolor("Yellow")
	Square()
	Circle()
	Triangle()
	window.exitonclick()
	
def circlofSquares():
	brad = turtle.Turtle()
	brad.color("Blue")
	for i in range(1,36):
		Triangle(brad)
		brad.left(10)

circlofSquares()