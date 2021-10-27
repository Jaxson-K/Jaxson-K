#   a116_bugglength_image.plength
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# create spider body
spider.pensize(40)
spider.circle(20)
# configure spider legs
spider.speed(0)
legs = 8
length = 70
angle = 290 / legs
spider.pensize(5)
# draw spider legs
n = 0
while (n < legs):
  spider.goto(0,20)
  spider.setheading(angle*n)
  spider.forward(length)
  n = n + 1
spider.backward(70)
spider.right(90)
spider.forward(25)
spider.right(90)
spider.pensize(1)
for x in range(8):
  spider.color("red")
  spider.begin_fill()
  spider.circle(1)
  spider.end_fill()
  spider.right(5)
  spider.color("black")
  spider.forward(5)

spider.hideturtle()
legsn = trtl.Screen()
legsn.mainloop()