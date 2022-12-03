from turtle import Turtle
import time
import random

ROW_INCREMENT = (100, 50)
STARTING_X = -270
STARTING_Y = 220
BLOCKADE_X = -420
BLOCKADE_Y = -300
BLOCK_INCREMENT = (300, 35)
COLORS = ["red", "orange", "yellow", "green", "blue"]
SHAPES = ["circle", "square", "circle", "square"]
START_INCREMENT = 5


class Board:
    def __init__(self):
        self.rows = []
        self.sideways_rows = []
        self.row_creation()
        self.blocks = []
        self.blockades()
        self.move_increment_rows = 0.5
        self.lasers = []
        print(len(self.rows))
        print(len(self.sideways_rows))

    def row_creation(self):
        for y in range(4):
            for i in range(7):
                block = Turtle()
                block.shape(SHAPES[y])
                block.speed(10)
                block.penup()
                block.color(COLORS[y])
                block.shapesize(stretch_wid=1, stretch_len=3)
                block.goto((STARTING_X + (ROW_INCREMENT[0] * i)), (STARTING_Y + (ROW_INCREMENT[1] * y)))
                self.rows.append(block)

    def blockades(self):
        for k in range(3):
            for x in range(4):
                block = Turtle()
                block.shape('square')
                block.speed(10)
                block.penup()
                block.color('green')
                block.shapesize(stretch_wid=1, stretch_len=4)
                block.goto((BLOCKADE_X + (BLOCK_INCREMENT[0] * x)), (BLOCKADE_Y + (BLOCK_INCREMENT[1] * k)))
                self.blocks.append(block)

    def forward_movement(self):
        for monster in self.rows:
            if self.rows[len(self.rows) - 1].xcor() >= 550:
                self.move_increment_rows += 0.2
                for monsters in self.rows:
                    monsters.sety(monsters.ycor() - 25)
                    monsters.setheading(180)
                for monsterz in self.rows:
                    monsterz.forward(self.move_increment_rows)

            elif monster.xcor() <= -550:
                self.move_increment_rows += 0.2
                for monsters in self.rows:
                    monsters.sety(monsters.ycor() - 25)
                    monsters.setheading(0)
                for monsterz in self.rows:
                    monsterz.forward(self.move_increment_rows)
                self.forward_movement()
            elif monster.xcor() < 550:
                monster.forward(self.move_increment_rows)

    def laser_creation(self):
        rand_num = random.choice(range(1, 170))
        rand_block = random.choice(self.rows)
        if rand_num == 5:
            laser = Turtle()
            laser.speed(6)
            laser.penup()
            laser.setheading(270)
            laser.setx(rand_block.xcor())
            laser.sety(rand_block.ycor())
            laser.color('red')
            laser.shape('square')
            self.lasers.append(laser)

    def laser_move(self):
        self.laser_creation()
        for laser in self.lasers:
            if laser.ycor() > -550:
                laser.forward(1)
            elif laser.ycor() <= -550:
                self.lasers.remove(laser)
