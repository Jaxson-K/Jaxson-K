#group members: Toma, Jaxson, Omar, Darryl
import turtle as trtl
t = trtl.Turtle()
#function for equation
def equation():
  equation = input("Equation in y=mx+b: ")
  m = int(equation[2])
  b = int(equation[5])
  b = b*20

  t.pensize(3)
  #first point
  x = 400 
  y = m*x+b
  t.penup()
  t.goto(x,y)
  t.pendown()

  t.goto(0,b)
#second point
  x = -400
  y = m*x+b

  t.goto(x,y)


#graphing lines
t.speed(0)
t.penup()
t.setposition(-390,400)
for i in range(40):
	t.right(90)
	t.pendown()
	t.forward(800)
	t.left(90)
	t.penup()
	t.forward(10)
	t.pendown()
	t.left(90)
	t.forward(800)
	t.right(90)
	t.penup()
	t.forward(10)

t.penup()
t.setposition(400,-390)
t.pendown()
t.right(270)
for i in range(40):
  t.left(90)
  t.pendown()
  t.forward(800)
  t.right(90)
  t.penup()
  t.forward(10)
  t.pendown()
  t.right(90)
  t.forward(800)
  t.left(90)  
  t.penup()
  t.forward(10)

t.penup()
t.setposition(0,0)
t.pendown()
t.color("red")
t.forward(400)
t.backward(800)
t.forward(400)
t.left(90)
t.forward(400)
t.backward(800)

#draw line of eqation
equation()

wn = trtl.Screen()
wn.mainloop()