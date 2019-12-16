import pygame
import sys
from Client import maze, player_maze, make_a_move
from Client import start, end, treasure

W = 640
H = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
PURPLE = (255, 0, 255)
LAVENDER = (230, 230, 250)
GREY = (230, 230, 250)
YELLOW = (255, 255, 0)

NODES = int(maze.number_of_nodes() ** 0.5)

maze_size = min(W, H)
steps = 0

step_x = maze_size // NODES
step_y = maze_size // NODES
side = step_x // 3
left_corner_x = step_x * 0.5 - side // 2
left_corner_y = step_y * 0.5 - side // 2

x = left_corner_x + step_x * (start[0] - 1)
y = left_corner_y + step_y * (start[1] - 1)

maze_x = (W - maze_size) // 2
maze_y = (H - maze_size) // 2

treasure_x = int(step_x * treasure[0] - left_corner_x - side // 2)
treasure_y = int(step_y * treasure[1] - left_corner_y - side // 2)

print(step_x)


def make_grid(width, height, screen):
    for point_x in range(0, height, step_y):
        pygame.draw.line(screen, GREY, (0, point_x), (width, point_x), 1)
    for point_y in range(0, width, step_x):
        pygame.draw.line(screen, GREY, (point_y, 0), (point_y, height), 1)


def move_x(screen, surface, rect, step, is_collected):
    curr_pos = (rect.x // step_x + 1, rect.y // step_y + 1)
    if step > 0:
        way = 3
        next_pos = (curr_pos[0] + 1, curr_pos[1])
        new_pos = make_a_move(maze, player_maze, next_pos, curr_pos)
    else:
        way = 9
        next_pos = (curr_pos[0] - 1, curr_pos[1])
        new_pos = make_a_move(maze, player_maze, next_pos, curr_pos)

    if new_pos == tuple(end[2:]):
        if is_collected:
            draw_wall(screen, rect, way, GREEN, 8)
            surface.fill(WHITE)
            screen.blit(surface, rect)
            rect.move_ip(step, 0)
            surface.fill(PURPLE)
            screen.blit(surface, rect)
        else:
            draw_wall(screen, rect, way, GREEN, 8)
    elif new_pos == curr_pos:
        draw_wall(screen, rect, way, BLACK, 3)
    else:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(step, 0)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


def move_y(screen, surface, rect, step, is_collected):
    curr_pos = (rect.x // step_x + 1, rect.y // step_y + 1)
    if step > 0:
        way = 6
        next_pos = (curr_pos[0], curr_pos[1] + 1)
        new_pos = make_a_move(maze, player_maze, next_pos, curr_pos)
    else:
        way = 0
        next_pos = (curr_pos[0], curr_pos[1] - 1)
        new_pos = make_a_move(maze, player_maze, next_pos, curr_pos)

    if new_pos == tuple(end[2:]):
        if is_collected:
            draw_wall(screen, rect, way, GREEN, 8)
            surface.fill(WHITE)
            screen.blit(surface, rect)
            rect.move_ip(0, step)
            surface.fill(PURPLE)
            screen.blit(surface, rect)
        else:
            draw_wall(screen, rect, way, GREEN, 8)
    elif new_pos == curr_pos:
        draw_wall(screen, rect, way, BLACK, 3)
    else:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(0, step)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


def draw_wall(screen, rect, way, color, width):
    if way == 0:
        start_x = rect.x - step_x / 2 + side // 2
        start_y = rect.y - step_y / 2 + side // 2
        end_x = rect.x + step_x / 2 + side // 2
        end_y = rect.y - step_y / 2 + side // 2
    elif way == 6:
        start_x = rect.x - step_x / 2 + side // 2
        start_y = rect.y + step_y / 2 + side // 2
        end_x = rect.x + step_x / 2 + side // 2
        end_y = rect.y + step_y / 2 + side // 2
    elif way == 3:
        start_x = rect.x + step_x / 2 + side // 2
        start_y = rect.y - step_y / 2 + side // 2
        end_x = rect.x + step_x / 2 + side // 2
        end_y = rect.y + step_y / 2 + side // 2
    elif way == 9:
        start_x = rect.x - step_x / 2 + side // 2
        start_y = rect.y - step_y / 2 + side // 2
        end_x = rect.x - step_x / 2 + side // 2
        end_y = rect.y + step_y / 2 + side // 2
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), width)


pygame.init()

background = pygame.display.set_mode((W, H))
background.fill(LAVENDER)

screen = pygame.Surface((maze_size, maze_size))
screen.fill(WHITE)

make_grid(W, H, screen)
player_rect = pygame.Rect((x, y, side, side))
player_surface = pygame.Surface((player_rect.width, player_rect.height))
player_surface.fill(PURPLE)

font1 = pygame.font.Font(None, 20)
steps_text = font1.render('Steps: ', 1, BLACK)
number_of_steps_text = font1.render(str(steps), 1, BLACK)
steps_rect = pygame.Rect((0, 0, step_x * 2, step_y * 2))

is_collected = False
treasure_text = font1.render('Treasure', 1, BLACK)
collected_text = font1.render('collected:', 1, BLACK)
is_collected_state_text = font1.render(str(is_collected), 1, BLACK)

pygame.draw.circle(screen, YELLOW, (treasure_x, treasure_y), side // 2)
screen.blit(player_surface, player_rect)
background.blit(screen, (maze_x, maze_y))
background.blit(steps_text, (5, 10))
background.blit(number_of_steps_text, (45, 10))
background.blit(treasure_text, (5, 40))
background.blit(collected_text, (5, 55))
background.blit(is_collected_state_text, (5, 75))
pygame.display.update()

game = True
is_over = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x(screen, player_surface, player_rect, step_x, is_collected)
                steps += 1
            elif event.key == pygame.K_LEFT:
                move_x(screen, player_surface, player_rect, -step_x, is_collected)
                steps += 1
            elif event.key == pygame.K_DOWN:
                move_y(screen, player_surface, player_rect, step_y, is_collected)
                steps += 1
            elif event.key == pygame.K_UP:
                move_y(screen, player_surface, player_rect, -step_y, is_collected)
                steps += 1

    if (player_rect.x // step_x + 1, player_rect.y // step_y + 1) == (end[2], end[3]):
        if is_collected:
            game = False
            is_over = True

    if (abs(player_rect.x - treasure_x) <= side) and (abs(player_rect.y - treasure_y) <= side):
        is_collected = True

    number_of_steps_text = font1.render(str(steps), 1, BLACK)
    pygame.draw.rect(background, LAVENDER, steps_rect)

    is_collected_state_text = font1.render(str(is_collected), 1, BLACK)

    background.blit(steps_text, (5, 10))
    background.blit(number_of_steps_text, (45, 10))
    background.blit(treasure_text, (5, 40))
    background.blit(collected_text, (5, 55))
    background.blit(is_collected_state_text, (5, 75))
    background.blit(screen, (maze_x, maze_y))
    pygame.display.update()

font2 = pygame.font.Font(None, 72)
is_over_text = font2.render("You've won!", 1, GREEN)

while is_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background.blit(is_over_text, (maze_size // 2 - 60, maze_size // 2 - 36))
    pygame.display.update()
