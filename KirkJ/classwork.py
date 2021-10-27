
circles = int(input("what is your favorite number?"))

import turtle as trtl

t = trtl.Turtle()

t.speed(0)
t.penup()
t.backward(200)
def circle():
  x = 0
  while( x <= circles):
   t.pendown()
   t.circle(10)
   t.penup()
   t.forward(20)
   x = x + 1
number = circles
circle()
number = number % 2
if number == 0:
  print("your number is even!")
elif number == 1:
  print("your number is odd!")
