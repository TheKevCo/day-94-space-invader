from turtle import Screen, Turtle
from board import Board
from player import Player

screen = Screen()
screen.title('Space Invaders')
screen.setup(width=1280, height=900)
screen.bgcolor('black')
screen.tracer(0)
board = Board()
player = Player()
screen.onkeypress(player.ball_create, "Up")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
game_on = True
screen.listen()

while game_on:
    try:
        board.forward_movement()
        player.ball_move()
        board.laser_move()
        screen.update()
        for block in board.rows:
            for ball in player.balls:
                if ball.distance(block) < 25:
                    block.setx(2000)
                    board.rows.remove(block)
                    ball.sety(800)

        for barricade in board.blocks:
            for laser in board.lasers:
                if laser.distance(barricade) < 35:
                    barricade.setx(2000)
                    board.blocks.remove(barricade)
                    laser.sety(-600)
        for player in player.the_player:
            for laser in board.lasers:
                if laser.distance(player) < 25:
                    player.sety(3000)
                    game_on = False
    except IndexError:
        game_on = False

screen.mainloop()
