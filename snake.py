import pygame, sys

pygame.init()

size = width, height = 320, 240
speed = [2,2]

# Colors

colorDict = {
    "BLACK": (0,0,0),
    "WHITE": (225,225,225),
    "GREEN": (0,225,0),
    "RED": (225,0,0)
}

screen = pygame.display.set_mode(size)

#gameLoop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
            break
    
    screen.fill(colorDict["WHITE"])
    
    pygame.display.flip()