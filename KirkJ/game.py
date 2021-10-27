# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
global score
spotColor = "pink"
spotShape = "circle"
spotSize = 2
score = 0
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
#-----game functions--------
def update_score():
  #score = score + 1
  print(score)

def spot_clicked(x,y):
  update_score()
  change_position()
  
def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
  


#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()