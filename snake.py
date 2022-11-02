import pygame, sys, random

pygame.init()

# Creating screen

window = pygame.display.set_mode((600,600))

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
        self.pos = [0, 0]
        self.speed = 1
        self.length = 1
        self.body = [[0,0]]
        self.scl = 30

    def update(self, direction):
        self.direction = direction
        
        if direction == "RIGHT":
            self.pos[0] += self.speed*self.scl
        if direction == "LEFT":
            self.pos[0] -= self.speed*self.scl
        if direction == "UP":
            self.pos[1] -= self.speed*self.scl
        if direction == "DOWN":
            self.pos[1] += self.speed*self.scl

        
        for i in range(self.length):
            self.body[-abs(i)]= self.body[-abs(i+1)]                 
            pygame.draw.rect(window, colors["GREEN"], (self.body[i][0], self.pos[i][1], self.scl, self.scl))
        

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
        

    def checkDeath(self):
        if (self.pos[0] < 0 or self.pos[0] > 600) or (self.pos[1] < 0 or self.pos[1] > 600):
            print("YOU DIED")
            sys.exit()

    def eatApple(self):
        self.body.append(self.body[-1] + [30, 30])

# apple

class Apple():
    def __init__(self):
        self.pos = [random.randrange(1,20)*30 ,random.randrange(1,20)*30]
        
    def spawnApple(self, newPos=False):
        if newPos:
            self.pos = [random.randrange(1,20)*30, random.randrange(1,20)*30]
 
        apple = pygame.Rect(self.pos[0], self.pos[1], 30, 30)

        pygame.draw.rect(window, colors["RED"], apple)

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

        
        window.fill(colors["WHITE"])
        pygame.draw.rect(window, colors["BLACK"], (0,0,600,600))

        snakePos = snake.pos[0] + snake.pos[1]
        applePos = apple.pos[0] + apple.pos[1]

        snake.checkDeath()
        snake.update(dir)

        print("X " + str(snake.pos[0]) + " Y " + str(snake.pos[1]))
        print("X " + str(apple.pos[0]) + " Y " + str(apple.pos[1]))


        if snake.pos[0] == apple.pos[0] and snake.pos[1] == apple.pos[1]:
                snake.eatApple()
                apple.spawnApple(newPos=True)
                print(str(snakePos))
                print(str(applePos))
            
        else:
            apple.spawnApple()

        pygame.display.flip()
        
        pygame.time.delay(250);
        clock.tick(60)

