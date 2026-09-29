from turtle import Turtle,Screen
from Snakes import Snake
from food import Food
from score import Score
import time
score=Score()
ema=Snake()
window=Screen()
window.setup(width=600,height=500)
window.bgcolor("black")
window.tracer(0)
food=Food()
game_on=True
while game_on:
    ema.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(ema.up,"Up")
    window.onkey(ema.down,"Down")
    window.onkey(ema.right,"Right")
    window.onkey(ema.left,"Left")
    if ema.head.distance(food) < 15:
        food.apper()
        ema.add()
        score.add_score()
    if ema.head.xcor()>270 or ema.head.xcor()<-280 or ema.head.ycor()>230 or ema.head.ycor()<-230:
        game_on=False 
        score.game_over()   
    for segment in ema.turtls[0:-1]:
        if ema.head.distance(segment)<10:
            game_on=False
            score.game_over()
window.exitonclick()