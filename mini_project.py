import turtle as trtl
t = trtl.Turtle()

def greeting(info):
  lst = info.split()
  print("Hello, " + lst[0] + ("! Let's draw a picture!"))

info = input("name hobby color")

greeting(info)

for i in range (4) :
  t.forward(400)
  t.right(90)




















wn = trtl.Screen()
wn.mainloop()
