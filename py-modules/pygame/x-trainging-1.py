import time

import pygame

pygame.init()
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# Set screen size
size = 1280, 640
width, height = size
screen = pygame.display.set_mode(size)
ball = pygame.image.load("/home/mostafa/Desktop/سارة.jpeg")
speed = [0.1, 0.1]
rect = ball.get_rect()
mouse_pos = (0,0)
clicks_history = []
last_mouse_down_pos = None
is_mouse_down_clicked = None # None when no event, True after mouse down, False after the mouse up 
last_mouse_up_pos = None

def dispatch_events():
    global mouse_pos, last_mouse_down_pos, last_mouse_up_pos, is_mouse_down_clicked
    # Events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Select event type
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down_clicked=True
            last_mouse_down_pos=event.dict["pos"]
            clicks_history.append(last_mouse_down_pos)
        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_down_clicked=False
            last_mouse_up_pos=event.dict["pos"]
        if event.type == pygame.MOUSEMOTION:
            # Fill screen color
            mouse_pos=event.dict["pos"]
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                clicks_history.pop()
        
        
        print("type:", event.type)
        print("dict:", event.dict)
        # Change window caption
        pygame.display.set_caption(f"{last_mouse_down_pos}, {last_mouse_up_pos}")
    return True



def update_drawing():
    global rect, bakcground, is_mouse_down_clicked
    screen.fill(bakcground)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    
    if is_mouse_down_clicked is True:
        pygame.draw.circle(screen, BLACK, last_mouse_down_pos, 10, 2)
        
    elif is_mouse_down_clicked is False:
        pygame.draw.line(screen, BLACK, last_mouse_down_pos, last_mouse_up_pos, 10)
        pygame.draw.rect(screen, BLACK, (
                                         min((last_mouse_down_pos[0] , last_mouse_up_pos[0])),
                                         min((last_mouse_down_pos[1] , last_mouse_up_pos[1])),
                                         abs(last_mouse_down_pos[0] - last_mouse_up_pos[0]),
                                         abs(last_mouse_down_pos[1] - last_mouse_up_pos[1]),
                                         ), 10)
        # is_mouse_down_clicked = None
    else:
        pygame.draw.circle(screen, RED, (500, 500), 10, 2)
    
    if len(clicks_history) > 1:
        bounding_rectangle = pygame.draw.lines(screen, RED, True, clicks_history, 3)
        pygame.draw.rect(screen, GREEN, bounding_rectangle, 1)
    
    pygame.draw.rect(screen, RED, (mouse_pos[0], mouse_pos[1], 120, 100))
    pygame.draw.rect(screen, GREEN, (mouse_pos[0]+100, 60, 120, 100))
    pygame.draw.rect(screen, BLUE, (150, mouse_pos[1]+100, 120, 100))
    
    pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
    pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
    pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)
    
    pygame.draw.rect(screen, RED, (650, 20, 100, 100), 1, 12)
    pygame.draw.rect(screen, GREEN, (700, 60, 100, 100), 4, 22)
    pygame.draw.rect(screen, BLUE, (750, 100, 100, 100), 8, 45)
    
    pygame.draw.rect(screen, RED, (800, 20, 120, 100), 1, 2, 10)
    pygame.draw.rect(screen, GREEN, (850, 60, 120, 100), 4, 4, -1, 20)
    pygame.draw.rect(screen, BLUE, (900, 100, 120, 100), 8, 8, -1, -1, 20)
    pygame.draw.rect(screen, BLACK, (950, 140, 120, 100), 8, 8, -1, -1, -1, 20)
    
    pygame.draw.ellipse(screen, RED, (50, 220, 160, 100))
    pygame.draw.ellipse(screen, GREEN, (100, 260, 160, 100))
    pygame.draw.ellipse(screen, BLUE, (150, 300, 160, 100))
    pygame.draw.ellipse(screen, RED, (350, 220, 160, 100), 1)
    pygame.draw.ellipse(screen, GREEN, (400, 260, 160, 100), 4)
    pygame.draw.ellipse(screen, BLUE, (450, 300, 160, 100), 8)
    
    pygame.display.update()

def update_state():
    global rect, bakcground
    
    bakcground = (mouse_pos[0] % 255, 100, mouse_pos[1] % 255)
    
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
        
def main_loop():
    while True:
        
        update_state()
        
        update_drawing()

        if dispatch_events() is False:
            break
        
    pygame.quit()

main_loop()
