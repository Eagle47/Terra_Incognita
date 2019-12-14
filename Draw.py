import pygame
import sys

FPS = 60
W = 640
H = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
NODES = 8

step_x = W // NODES
step_y = H // NODES
side = 20
x = W // NODES * 0.5 - side // 2
y = H // NODES * 0.5 - side // 2


def make_grid(width, height, screen):
    for point_x in range(0, height + 1, height // NODES):
        pygame.draw.line(screen, BLACK, (0, point_x), (width, point_x), 1)
    for point_y in range(0, width + 1, width // NODES):
        pygame.draw.line(screen, BLACK, (point_y, 0), (point_y, height), 1)


def move_x(screen, surface, rect, step):
    if 0 <= (rect.x + step) <= W:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(step, 0)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


def move_y(screen, surface, rect, step):
    if 0 <= (rect.y + step) <= H:
        surface.fill(WHITE)
        screen.blit(surface, rect)
        rect.move_ip(0, step)
        surface.fill(PURPLE)
        screen.blit(surface, rect)


pygame.init()
screen = pygame.display.set_mode((W, H))

screen.fill(WHITE)
make_grid(W, H, screen)
player_rect = pygame.Rect((x, y, side, side))
player_surface = pygame.Surface((player_rect.width, player_rect.height))
player_surface.fill(PURPLE)
screen.blit(player_surface, player_rect)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x(screen, player_surface, player_rect, step_x)
            elif event.key == pygame.K_LEFT:
                move_x(screen, player_surface, player_rect, -step_x)
            elif event.key == pygame.K_DOWN:
                move_y(screen, player_surface, player_rect, step_y)
            elif event.key == pygame.K_UP:
                move_y(screen, player_surface, player_rect, -step_y)

    pygame.display.update()
