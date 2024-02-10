import turtle
class Plate(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.createplate()
    def createplate(self):
        self.penup()
        self.color('white')
        self.shape('square')
        self.goto(0,-260)
        self.shapesize(stretch_wid=1,stretch_len=4)
    def moveright(self):
        if self.xcor()<280:
            self.forward(20)
    def moveleft(self):
        if self.xcor()>-280:
            self.backward(20)
