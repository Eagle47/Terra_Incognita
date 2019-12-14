import pygame
import sys
from Core import make_a_move, is_over
from Client import maze, player_maze, start, end, number_of_nodes

W = 640
H = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
LAVENDER = (230, 230, 250)
GREY = (230, 230, 250)

NODES = number_of_nodes

maze_size = min(W, H)
steps = 0

step_x = maze_size // NODES
step_y = maze_size // NODES
side = 20
left_corner_x = step_x * 0.5 - side // 2
left_corner_y = step_y * 0.5 - side // 2

x = left_corner_x + step_x * (start[0] - 1)
y = left_corner_y + step_y * (start[1] - 1)

maze_x = (W - maze_size) // 2
maze_y = (H - maze_size) // 2


def make_grid(width, height, screen):
    for point_x in range(0, height, step_y):
        pygame.draw.line(screen, GREY, (0, point_x), (width, point_x), 1)
    for point_y in range(0, width, step_x):
        pygame.draw.line(screen, GREY, (point_y, 0), (point_y, height), 1)


def move_x(screen, surface, rect, step):
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
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(step, 0)
        surface.fill(PURPLE)
        screen.blit(surface, rect)
        pygame

    if new_pos == curr_pos:
        draw_wall(screen, rect, way)
    elif 0 <= (rect.x + step) <= W:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(step, 0)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


def move_y(screen, surface, rect, step):
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
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(1000, 1000)
        surface.fill(PURPLE)
        screen.blit(surface, rect)

    if new_pos == curr_pos:
        draw_wall(screen, rect, way)
    elif 0 <= (rect.y + step) <= H:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(0, step)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


def draw_wall(screen, rect, way):
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
    pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 3)


pygame.init()

background = pygame.display.set_mode((W, H))
background.fill(LAVENDER)

screen = pygame.Surface((maze_size, maze_size))
screen.fill(WHITE)

make_grid(W, H, screen)
player_rect = pygame.Rect((x, y, side, side))
player_surface = pygame.Surface((player_rect.width, player_rect.height))
player_surface.fill(PURPLE)

font = pygame.font.Font(None, 20)
steps_text = font.render('Steps: ', 1, BLACK)
number_of_steps_text = font.render(str(steps), 1, BLACK)
steps_rect = pygame.Rect((0, 0, step_x, step_y))

screen.blit(player_surface, player_rect)
background.blit(screen, (maze_x, maze_y))
background.blit(steps_text, (5, 10))
background.blit(number_of_steps_text, (45, 10))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x(screen, player_surface, player_rect, step_x)
                steps += 1
            elif event.key == pygame.K_LEFT:
                move_x(screen, player_surface, player_rect, -step_x)
                steps += 1
            elif event.key == pygame.K_DOWN:
                move_y(screen, player_surface, player_rect, step_y)
                steps += 1
            elif event.key == pygame.K_UP:
                move_y(screen, player_surface, player_rect, -step_y)
                steps += 1

    number_of_steps_text = font.render(str(steps), 1, BLACK)
    pygame.draw.rect(background, LAVENDER, steps_rect)

    background.blit(steps_text, (5, 10))
    background.blit(number_of_steps_text, (45, 10))
    background.blit(screen, (maze_x, maze_y))
    pygame.display.update()
