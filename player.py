from turtle import Turtle

STARTING_POSITION = (0, -400)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('turtle')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setheading(90)
        self.reset()
        self.balls = []
        self.the_player = [self]

    def reset(self):
        self.goto(STARTING_POSITION)

    def move_right(self):
        self.setx(self.xcor() + 30)

    def move_left(self):
        self.setx(self.xcor() - 30)

    def ball_create(self):
        ball = Turtle()
        ball.speed(10)
        ball.penup()
        ball.setx(self.xcor())
        ball.sety(self.ycor())
        ball.setheading(90)
        ball.color('white')
        ball.shape('circle')
        self.balls.append(ball)
        self.ball_move()

    def ball_move(self):
        for ball in self.balls:
            if ball.ycor() < 550:
                ball.forward(5)
            elif ball.ycor() >= 550:
                self.balls.remove(ball)
