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
incrementing_counter= 0
while (incrementing_counter< leg_amount):
  spider.goto(0,0)
  spider.setheading(leg_angle*incrementing_counter)
  spider.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
spider.hideturtle()

leg_amountn = trtl.Screen()