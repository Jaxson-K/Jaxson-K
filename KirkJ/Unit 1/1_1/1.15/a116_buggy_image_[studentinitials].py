#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

leg_amount = 8
leg_length= 70

leg_angle = 380 / leg_amount
spider.pensize(5)
n = 0
while (n < leg_amount):
  spider.goto(0,0)
  spider.setheading(leg_angle*n)
  spider.forward(leg_length)
  n = n + 1
spider.hideturtle()

leg_amountn = trtl.Screen()