import pygame
pygame.init()

class Monster:
    def __init__(self, x, y, w, h, filename):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
    
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])

class Platform:
    def __init__(self, x, y, w, h, filename, speed):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
    
    def draw(self, screen):
        screen.blit(self.png, [self.rect.x,self.rect.y])


class Ball:
    def __init__(self, x, y, w, h, filename, speedX,  speedY):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speedX = speedX
        self.speedY = speedY
    
    def draw(self, screen): 
        screen.blit(self.png, [self.rect.x,self.rect.y])

#створити екран
screen = pygame.display.set_mode((500, 500)) 
#створити інструмент для обмеження фпс
fps = pygame.time.Clock()
monsters = []
x = 20
for i in range(6):
    monsters.append( Monster(x, 0, 50, 50, "pixilart-drawing (2).png"))
    x += 100

x = 20
for i in range(6):
    monsters.append( Monster(x, 150, 50, 50, "pixilart-drawing (2).png"))
    x += 100
ball = Ball(400, 250, 50, 50, "pixil-frame-0 (1) (1).png", 5, 5)
platform = Platform(250, 300, 100, 20, "pixil-frame-0 (2) (1).png", 0)
#ігровий цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                platform.speed = 5
            if event.key == pygame.K_LEFT:
                platform.speed = -5

    #ОНОвлення
    if len(monsters) ==0:
        screen.fill((255, 213, 195))
        winLable = pygame.font.Font(None, 50).render("Ти виграв!", True, (255, 255, 255))
        screen.blit(winLable, [250, 250])
        pygame.display.flip()
        break
    platform.rect.x +=  platform.speed
    
    ball.rect.x += ball.speedX
    ball.rect.y += ball.speedY

    if  ball.rect.x > 500:
        ball.speedX *= -1
    
    if  ball.rect.y > 500:
        ball.speedY *= -1
    if ball.rect.x < 0:
        ball.speedX *= -1
    if ball.rect.y < 0:
        ball.speedY *= -1

    if platform.rect.colliderect(ball.rect): 
       ball.speedY *= -1 
    for i in range( len(monsters) ):
        if monsters[i].rect.colliderect(ball.rect):
              ball.speedY *= -1
              monsters.pop(i)
              break
    

    #якщо мяч зіткнувся з платформою
        #відбити мяч по y
    #рендер
    
    screen.fill((247, 218, 221)) 
    for i in range( len(monsters) ):
        monsters[i].draw(screen)
    ball.draw(screen)
    platform.draw(screen)
    pygame.display.flip()

    #обмежити фпс

    fps.tick(60)
