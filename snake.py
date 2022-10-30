import pygame, sys, random

pygame.init()

# Creating screen

size = width, hight = 600, 600

window = pygame.display.set_mode(size)

# Color dictionary

colors = {
        "RED": (225, 0, 0),
        "GREEN": (0, 225, 0),
        "BLUE": (0, 0, 225)
}

class Snake():
    def __init__(self):
        self.direction = "RIGHT"
        self.head = x, y = 300, 300

    def update(self):
        head = pygame.Rect(self.head.x, self.head.y, 6, 6)
        pygame.draw.rect(window, colors["GREEN"], head)
        pygame.display.flip()

class Apple():
    def __init__(self):
        pass
if "__name__" == __main__:
    gameLoop = True

    snake = Snake()
    apple = Apple()

    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
                gameLoop = False

