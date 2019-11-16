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
        self.color('green')
        self.penup()
        self.speed('fastest')

    def up(self):
        x_new = self.xcor()
        y_new = self.ycor() + 24

        if (x_new, y_new) not in walls:
            self.goto(x_new, y_new)

    def down(self):
        x_new = self.xcor()
        y_new = self.ycor() - 24

        if (x_new, y_new) not in walls:
            self.goto(x_new, y_new)

    def left(self):
        x_new = self.xcor() - 24
        y_new = self.ycor()

        if (x_new, y_new) not in walls:
            self.goto(x_new, y_new)

    def right(self):
        x_new = self.xcor() + 24
        y_new = self.ycor()

        if (x_new, y_new) not in walls:
            self.goto(x_new, y_new)

    def is_collision(self, obj):
        dx = self.xcor() - obj.xcor()
        dy = self.ycor() - obj.ycor()
        distance = (dx ** 2 + dy ** 2) ** (1/2)

        if distance == 0:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.speed('fastest')

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()


lvl = [
    'WWWWWWWWWWWWWWW',
    'WPW    WWW   WW',
    'W   WW   WWW WW',
    'WWWWWW WWW   WW',
    'WT     WWW WWWW',
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
                walls.append((screen_x, screen_y))

            if cell == 'P':
                player.goto(screen_x, screen_y)

            if cell == 'T':
                treasure.goto(screen_x, screen_y)


pen = Pen()
player = Player()
treasure = Treasure()

walls = []

create_maze(lvl)

turtle.listen()
turtle.onkey(player.left, "a")
turtle.onkey(player.right, 'd')
turtle.onkey(player.up, 'w')
turtle.onkey(player.down, 's')

while True:
    if player.is_collision(treasure):
        print('Treasure collected!')
        treasure.destroy()

    window.update()
