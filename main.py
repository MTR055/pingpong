import turtle as t
import ball
import time
import plate
import scoreboard
import createboundary
my_screen=t.Screen()
my_screen.screensize(300,300)
my_screen.bgcolor('Black')
my_screen.tracer(0)

score=scoreboard.Scoreboard()
playball=ball.Ball()
catcher=plate.Plate()
boundary=createboundary.Create_boundary()
my_screen.onkey(catcher.moveright,'Right')
my_screen.onkey(catcher.moveleft,'Left')
my_screen.listen()
game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.05)
    playball.moveball()
    if playball.xcor() > 300 or playball.xcor() < -300 :
        playball.change_colour()
        playball.change_directionx()
    if playball.ycor() > 240 :
        playball.change_directiony()
        playball.change_colour()
    if (abs(playball.xcor()-catcher.xcor()) < 40 and playball.ycor()-catcher.ycor()<20):
        playball.change_directiony()
        score.update_score()
    if playball.ycor()<-260:
        score.game_over()
        game_is_on=False





















my_screen.exitonclick()