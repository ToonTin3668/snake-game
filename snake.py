import pygame, sys, random

pygame.init()

# Creating screen

size = width, hight = 600, 600

window = pygame.display.set_mode(size)

# Time
clock = pygame.time.Clock()

# Color dictionary

colors = {
        "RED": (225, 0, 0),
        "GREEN": (0, 225, 0),
        "BLUE": (0, 0, 225),
        "BLACK": (0,0,0),
        "WHITE": (225,225,225)
}

# Snake

class Snake():
    def __init__(self):
        self.x, self.y = 300, 300
        self.speed = 1
        self.scl = 30

    def update(self, direction):
        self.direction = direction
        
        if direction == "RIGHT":
            self.x += self.speed*self.scl
        if direction == "LEFT":
            self.x -= self.speed*self.scl
        if direction == "UP":
            self.y -= self.speed*self.scl
        if direction == "DOWN":
            self.y += self.speed*self.scl

        head = pygame.Rect(self.x, self.y, self.scl, self.scl)
        pygame.draw.rect(window, colors["GREEN"], head)
        print("X " + str(self.x) + " Y " + str(self.y))
        pygame.display.flip()


    def getInput(self, evt):
        if evt.key == pygame.K_RIGHT:
            self.direction = "RIGHT"
        if evt.key == pygame.K_LEFT:
            self.direction = "LEFT"
        if evt.key == pygame.K_UP:
            self.direction = "UP"
        if evt.key == pygame.K_DOWN:
            self.direction = "DOWN"
        return self.direction
        

    def die(self):
        if self.x <= 0 or self.x >= 600:
            print("YOU DIED")
            sys.exit()
        if self.y <= 0 or self.y >= 600:
            print("YOU DIED")
            sys.exit()

# apple

class Apple():
    def __init__(self):
        self.x = round(random.randint(1,300)/30)
        self.y = round(random.randint(1,300)/30)
    
    def spawnApple(self):
        self.x = round(random.randint(1,300)%30)
        self.y = round(random.randint(1,300)%30)

        apple = pygame.Rect(self.x, self.y, 30, 30)

        pygame.draw.rect(window, colors["RED"], apple)
        pygame.display.flip();

if __name__ == "__main__":
    gameLoop = True

    snake = Snake()
    apple = Apple()

    dir = "RIGHT"

    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
                gameLoop = False
            if event.type == pygame.KEYDOWN:
                dir = snake.getInput(event)

        apple.spawnApple()
        window.fill(colors["BLACK"])
        snake.update(dir)
        snake.die()
        pygame.time.delay(500);
        clock.tick(60)

