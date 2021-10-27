import turtle as trtl

#global score
score = 0 
def spot_score():
  score += 1
  print(score)
def spot_clicked():
  spot.penup()
  spot.goto(randint(-100,0),randint(0,100))

# circular turtle will not use a global variable
spot = trtl.Turtle()
spot.penup()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)
# does not have access to the score that was created above

spot.onclick(spot_clicked)