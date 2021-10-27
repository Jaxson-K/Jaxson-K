#   a116_bugglength_image.plength
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# create spider body
spider.pensize(40)
spider.circle(20)
# configure spider legs
legs = 4
length = 70
angle = 375 / legs
spider.pensize(5)
# draw spider legs
n = 0
while (n < legs):
  spider.goto(0,20)
  spider.setheading(angle*n)
  spider.circle(50,80)
  spider.circle(50,-80)
  n = n + 1
for x in range(4):
  spider.goto(0,20)
  spider.left(20)
  spider.setheading(angle*n)
  spider.circle(-50,80)
  spider.circle(-50,-80)

spider.backward(length)
spider.right(20)
spider.forward(50)
spider.begin_fill()
spider.circle(20)
spider.end_fill()
spider.hideturtle()
legsn = trtl.Screen()
legsn.mainloop()