#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()


# create ladybug head

ladybug.pensize(40)
ladybug.circle(5)
ladybug.speed(0)
#make the legs
legs = 6
length = 70
angle = 380 / legs
ladybug.pensize(5)
# draw ladybug legs
n = 0
while (n < legs):
  ladybug.goto(0,-20)
  ladybug.setheading(angle*n)
  ladybug.forward(length)
  n = n + 1
ladybug.backward(length)
ladybug.left(20)
# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots += 1
ladybug.pensize(3)
  # position next dots
xpos = ypos + 25
xpos = xpos + 5
ladybug.penup()
ladybug.left(180)
ladybug.forward(15)
ladybug.right(90)
ladybug.pendown()
ladybug.begin_fill()
ladybug.circle(5)
ladybug.end_fill()
ladybug.penup()
ladybug.left(180)
ladybug.forward(30)
ladybug.left(90)
ladybug.forward(10)
ladybug.right(90)
ladybug.pendown()
ladybug.begin_fill()
ladybug.circle(5)
ladybug.end_fill()
ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()