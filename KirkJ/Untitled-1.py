'''
Group #1 Linear Graphing Calculator.

Requirements:
1. Comments explaing WHY you added a chunk of code
2. Fufillment of goal
3. Code must be written to transmit data to other sections / must easily work and fit in to other parts
'''

# Imports
import turtle as trtl
import math as math

# Painter 
painter = trtl.Turtle()
painter.speed(0)

painter.color("lightgrey")


y = -200

# Y Axis grid lines (10 increments)
for i in range(40):
  painter.penup()
  painter.setpos(-200, y)
  painter.pendown()
  
  # move forward
  painter.forward(400)
    
  y += 10
  
x = -200
painter.left(90)
  
# X Axis grid lines (10 increments)
for i in range(40):
  painter.penup()
  painter.setpos(x, -200)
  painter.pendown()
  
  # move forward
  painter.forward(400)
    
  x += 10
  


painter.penup()
painter.color("black")

# X Axis:
painter.goto(-200,0)
painter.pendown()
painter.goto(200,0)

# Y Axis:
painter.goto(0, 0) # Center
painter.goto(0, 200)
painter.goto(0,-200)

    

# User Input:

main_input = input("please input an equation in the form of (y = mx + B) where M and B are numbers (include spaces) ")
# Turn main input into a list
main_list = main_input.split()
print(main_list)

# find M and B variables
# int(main_list[2].split('x')[0])

slope = 0
y_intercept = float(main_list[4])

slope_list = main_list[2].split('x')[0].split('/')
print(slope_list)
if len(slope_list) > 1:
  slope = int(slope_list[0]) / int(slope_list[1])
else:
  slope = float(slope_list[0])

if main_list[3] == '-':
  y_intercept = -y_intercept

print("slope: ", str(slope))
print("y_intercept: ", str(y_intercept))

# User Input Variables to transmit: slope, y_intercept

# Required vars: y_intercept, slope
# Intercepts:

formulavar = -1 * y_intercept
x_intercept = formulavar/slope
print(x_intercept, y_intercept)

# Intercept Variables to transmit:
# x_intercept

# Line:
painter.pencolor('red')

# y and x intercepts
painter.penup()
painter.goto(1, y_intercept)
painter.pendown()
painter.circle(1)
painter.penup()
painter.goto(x_intercept, 0)
painter.pendown()
painter.circle(1)
painter.penup()


# Line
left_arrow_cor = (-200, slope*-200 + y_intercept) # position for left arrow stored in tupley 

# TODO add arrows, optimize by changing while conditions based on slope sign

length = 0
i = -200
while painter.xcor() <= 200:
  painter.goto(i, slope*i + y_intercept)
  painter.pendown()

  length += 1
  i += 1

print(length)
rot = math.degrees(math.atan(painter.ycor()/painter.xcor()))
painter.setheading(rot)

painter.stamp()
painter.penup()
painter.left(180)
painter.forward(length)
painter.pendown()
painter.stamp()
  

# Line Variables to transmit:
# none

# Main
if __name__ == "__main__":
  wn = trtl.Screen()
  wn.mainloop()
