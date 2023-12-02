def hello():
  print("hello")
def pack(lunches, snack, drink):
  return [lunches, snack, drink]
def eat_lunch(l):
  if len(l) == 0:
    print("my lunchbox is empty!")
  else:
    for i in range(len(l)):
      if i==0:
        print("first I'm eating", l[i])
      else: 
        print("then I'm eating", l[i])
      


hello()
pack("sandwich", "apple", "coke")
eat_lunch([])
eat_lunch(["sandwhich", "apple", "bananna", "candy"])

