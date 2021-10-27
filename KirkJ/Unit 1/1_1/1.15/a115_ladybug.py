#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)


# ladybug leg
leg_amount = 3
leg_length = 35*3/2

leg_angle = 30
ladybug.pensize(5)
incrementing_counter= 1
while (incrementing_counter< leg_amount+1):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*incrementing_counter-240)
  ladybug.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
ladybug.hideturtle()

leg_amount = 4

leg_angle = -30
incrementing_counter= 1
while (incrementing_counter< leg_amount):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*incrementing_counter+60)
  ladybug.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
ladybug.hideturtle()

ladybug.setheading(0)


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
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()