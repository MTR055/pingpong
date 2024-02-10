import turtle
import random
colours=['Gainsboro','CornflowerBlue','Blue','Aquamarine','MediumSeaGreen','PaleGreen','SpringGreen',
         'GreenYellow','Lime','OliveDrab','Beige','Khaki','LightYellow','Cornsilk','Yellow','Gold','DarkGoldenrod',
         'Orange','PeachPuff','Coral','OrangeRed','HotPink','LavenderBlush','Violet','MediumVioletRed','MediumOrchid',
         'MediumPurple','DeepPink','LawnGreen']
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.createball()


    def createball(self):
        self.shape('circle')
        self.color('White')
        self.penup()
        self.goto(0,-240)
        self.setheading(45)
        self.distancex = 10
        self.distancey = 10

    def moveball(self):
        newx=self.xcor()+self.distancex
        newy=self.ycor()+self.distancey
        self.goto(newx,newy)
    def change_directionx(self):
        self.distancex*=-1
    def change_directiony(self):
        self.distancey*=-1
    def change_colour(self):
        self.color(random.choice(colours))

