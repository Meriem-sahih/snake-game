from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtls=[]
        self.position=[(-40,0),(-20,0),(0,0)]
        self.body_snake()
        self.head=self.turtls[-1]
    def body_snake(self):
        for i in range(len(self.position)):
          body=Turtle("square")
          body.color("white")
          body.penup()
          body.goto(self.position[i])
          self.turtls.append(body)
    def move(self):
        for i in range(len(self.turtls)-1):
            self.turtls[i].goto(self.turtls[i+1].pos())  
        self.head.forward(20)
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)
    def add(self):
      new_turtle=Turtle()
      new_turtle.shape("square")
      new_turtle.color("white")
      new_turtle.penup()
      new_turtle.goto(self.turtls[0].pos()) 
      self.turtls.insert(0,new_turtle)   
       