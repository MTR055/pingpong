import turtle
class Create_boundary(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.create_boundary()

    def create_boundary(self):
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(320, -260)
        self.pendown()
        self.pensize(3)
        self.goto(320, 260)
        self.goto(-320, 260)
        self.goto(-320, -260)