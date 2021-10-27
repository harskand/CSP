import turtle as trtl

painter=trtl.Turtle()
painter.speed(0)
painter.pensize(5)

x=-150
y=-150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y= y + 5
  rem=floor%3
  if (rem==0):
    painter.color("blue") 
  rem=floor%2
  if (rem==0):
    painter.color("skyblue") 
  painter.stamp()
  floor = floor + 1

  painter.pendown()
  painter.forward(50)

x=-75
y=-150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y= y + 5
  rem=floor%3
  if (rem==0):
    painter.color("red") 
  painter.stamp()
  floor = floor + 1

  painter.pendown()
  painter.forward(50)

x= 0
y=-150

num_floors = 21
floor = 0

while floor < num_floors:
  painter.penup()
  painter.goto(x,y)
  painter.color("gray")
  y= y + 5
  rem=floor%3
  if (rem==0):
    painter.color("pink") 
  painter.stamp()
  floor = floor + 1

  painter.pendown()
  painter.forward(50)
wn = trtl.Screen()
wn.mainloop()