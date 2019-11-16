import turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(600, 600)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed('fastest')


lvl = [
    'WWWWWWWWWWWWWWW',
    'WPW    WWW   WW',
    'W   WW   WWW WW',
    'WWWWWW WWW   WW',
    'W      WWW WWWW',
    'WW WWWWWWW    W',
    'WW WW   WWWWW W',
    'WW    W       W',
    'WWWWW WWWW WWWW',
    'W   W      W WW',
    'W WWW WWWWWW  W',
    'W  WW    WW W W',
    'WW WWWWW WW W W',
    'WW            W',
    'WWWWWWWWWWWWWWW',
]


def create_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            cell = level[y][x]
            screen_x = -168 + (x * 24)
            screen_y = 168 - (y * 24)

            if cell == 'W':
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if cell == 'P':
                player.goto(screen_x, screen_y)


pen = Pen()
player = Player()

create_maze(lvl)

while True:
    pass
