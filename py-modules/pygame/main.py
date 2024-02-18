# https://stackoverflow.com/questions/50534617/draw-a-line-in-pygame
# https://www.w3schools.com/python/ref_math_sin.asp
# https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions
# https://github.com/CharlesPikachu/Games
# https://stackoverflow.com/questions/44835909/cannot-import-name-imagetk-python-3-5
# imports the pygame library module

import math

import pygame  # initilize the pygame module

SQUARE_UP = 250
SQUARE_LEFT = 250
SQUARE_WIDTH = 90
SQUARE_HIEGHT = 90
square = [
    (SQUARE_LEFT, SQUARE_UP),
    (SQUARE_LEFT + SQUARE_WIDTH, SQUARE_UP),
    (SQUARE_LEFT + SQUARE_WIDTH, SQUARE_UP + SQUARE_HIEGHT),
    (SQUARE_LEFT, SQUARE_UP + SQUARE_HIEGHT),
]
points = [(10, 10), (100, 10), (100, 100), (10, 100)]

BACKGROUND_COLOR = (80, 80, 255)
clock = pygame.time.Clock()


def main_square(color=(0, 0, 0)):
    global points
    # pygame.draw.line(display_screen, (0, 0, 0), (0, 0), (100, 100))
    pygame.draw.polygon(display_screen, color, points, 10)
    pygame.display.flip()


def handle_events(display_screen: pygame.surface.Surface):
    for events in pygame.event.get():
        if events.type == pygame.MOUSEMOTION:
            continue
            x, y = pygame.mouse.get_pos()
            for index, point in enumerate(square):
                points[index] = (point[0] + x, point[1] + y)
            display_screen.fill(BACKGROUND_COLOR)
            main_square((x % 256, y % 256, x % 256))
            # pygame.draw.line(
            #     display_screen, (x % 256, y % 256, 0), (xx, yy), (x, y)
            # )
            # xx = x
            # yy = y
            pygame.display.flip()
        if events.type == pygame.QUIT:
            pygame.quit()  # End the program
            quit()


def update_points(frame_counter):
    global square, points

    for index, point in enumerate(square):
        x_ = point[0] * math.cos(math.radians(frame_counter)) - point[1] * math.sin(
            math.radians(frame_counter)
        )
        y_ = point[0] * math.sin(math.radians(frame_counter)) + point[1] * math.cos(
            math.radians(frame_counter)
        )
        points[index] = (x_, y_)


def event_loop(display_screen: pygame.surface.Surface):
    global points

    line_color = (255, 0, 0)
    xx, yy = 0, 0
    frame_counter = 0
    while True:
        clock.tick(60)
        print("tick ", frame_counter)
        update_points(frame_counter)
        display_screen.fill(BACKGROUND_COLOR)  # Clear screen
        main_square()
        handle_events(display_screen)
        frame_counter += 1


pygame.init()  # Setting your screen size with a tuple of the screen width and screen height
display_screen = pygame.display.set_mode(
    (800, 600)
)  # Setting a random caption title for your pygame graphical window.
display_screen.fill(BACKGROUND_COLOR)
pygame.display.set_caption("pygame test")  # Update your screen when required
# pygame.display.flip()
pygame.display.update()  # quit the pygame initialization and module

main_square()

event_loop(display_screen)
