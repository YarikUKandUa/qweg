from pygame import *

def gameOver(screen, text):
    myfont = font.Font(None, 36).render(text, True, (0, 0, 0))
    clock = time.Clock()
    run = True
    while run:
        #події
        for e in event.get():
            if e.type == QUIT:
                run = False
        #оновлення

        #рендер
        screen.blit(myfont, [250, 250])
        display.update()
        clock.tick(60)

class Sprite:
    def __init__(self, x, y, filename, speed, w, h):
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, window):
        window.blit(self.image, ( self.rect.x,  self.rect.y))


class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed


class Bot(Sprite):
    def __init__(self, x, y, filename, speed, w, h, startX, finishX):
        super().__init__(x, y, filename, speed, w, h)
        self.startX = startX
        self.finishX = finishX

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= self.finishX:
            self.speed *= -1
        if self.rect.x <= self.startX:
            self.speed *= -1


class Wall:
    def __init__(self, x, y, w, h, color):
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

init()

mixer.init()
mixer.music.load("jungles (1).ogg")
mixer.music.play(-1)

kick = mixer.Sound('kick.ogg')
win = mixer.Sound('zombie-moaning-101369.mp3')

window = display.set_mode((700, 500))
clock = time.Clock()

walls = []
walls.append(Wall(0, 0, 10, 680, (105, 51, 0)))
walls.append(Wall(790, 0, 10, 600, (102, 51, 0)))
walls.append(Wall(690, 0, 10, 600, (102, 51, 0)))
walls.append(Wall(0, 490, 780, 10, (102, 51, 0)))

walls.append(Wall(10, 0, 790, 10, (102, 51, 0)))
walls.append(Wall(0, 200, 110, 10, (102, 51, 0)))
walls.append(Wall(0, 590, 600, 10, (102, 51, 0)))
walls.append(Wall(450, 350, 10, 250, (102, 51, 0)))
walls.append(Wall(500, 450, 250, 10, (102, 51, 0)))

walls.append(Wall(235, 200, 690, 10, (102, 51, 0)))

player = Player(145, 200, "pixil-frame-0 (3).png", 3, 50, 50)
npc = Bot(200, 250, "pixil-frame-0 (1).png", 1, 50, 50, 100, 500)
gold = Sprite(500, 400, "beer.png", 0, 50, 50)

run = True
while run:
    #події
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
            print(mouse.get_pos())
    #оновлення
    player.update()
    npc.update()

    if player.rect.colliderect(npc.rect):
        kick.play()
        gameOver(window, "MY BOY!!!")
        run = False

    for wall in walls:
        if wall.rect.colliderect(player.rect):
            kick.play()
            gameOver(window, "MY BOY!!!")
            run = False

    if player.rect.colliderect(gold.rect):
        win.play()
        gameOver(window, "YAAA!!!")
        run = False

    #рендер
    window.fill((128, 29, 29))
    player.draw(window)
    npc.draw(window)
    gold.draw(window)

    for wall in walls:
        wall.draw(window)
    display.update()

    clock.tick(60)






