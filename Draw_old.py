import pygame

number_of_nodes = 8


def screen_init(width, height):
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    background = background.convert()

    return screen, background


def make_grid(width, height, background):
    for point_x in range(0, height + 1, height // number_of_nodes):
        pygame.draw.line(background, (255, 0, 0), (0, point_x), (width, point_x), 1)
    for point_y in range(0, width + 1, width // number_of_nodes):
        pygame.draw.line(background, (255, 0, 0), (point_y, 0), (point_y, height), 1)


def display_flip():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        pygame.display.flip()
