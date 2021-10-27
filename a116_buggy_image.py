#   a116_bugglength_image.plength
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()
spider.pensianglee(40)
spider.circle(20)
legs = 6
length = 70
angle = 380 / legs
spider.pensianglee(5)
n = 0
while (n < legs):
  spider.goto(0,0)
  spider.setheading(angle*n)
  spider.forward(length)
 ''' n = n + 1
spider.hideturtle()
wn = trtl.Screen()'''
wn.mainloop()