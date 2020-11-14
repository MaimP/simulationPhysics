import pygame


class Circle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill(color)

        self.rect = self.image.get_rect()


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 400))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()


class mathMakesFun(pygame.sprite.Sprite):
    def calculateSpeedCollision(self):
        sumM = self.mass_1 + self.mass_2
        newV_1 = (self.mass_1 - self.mass_2)/sumM * self.speed_1
        newV_2 = (self.mass_2-self.mass_1)/sumM * self.speed_2
        newV_1 += ((2 * self.mass_2 / sumM) * self.speed_2)
        newV_2 += ((2 * self.mass_1 / sumM) * self.speed_1)
        self.speed_1 = newV_1
        self.speed_2 = newV_2
        print("speed nach collision ball: ", self.speed_1, self.speed_2)
        self.counter_collision += 1
        print("collisionen insgesamt: ", self.counter_collision)

    def calculateSpeedWall(self, which):
        if which == "x1":
            self.speed_1 = float(self.speed_1 * (-1))
        elif which == "x2":
            self.speed_2 = self.speed_2 * (-1)
        else:
            print("fehler calculateSpeedWall")

    def calculatePosition(self):
        pos_1_old = self.pos_1_float
        pos_2_old = self.pos_2_float
        self.pos_1_float = self.speed_1 + pos_1_old
        self.pos_2_float = self.speed_2 + pos_2_old
        pos_1_old = self.pos_1_float
        pos_2_old = self.pos_2_float
        self.x_1 = self.pos_1_float
        self.x_2 = self.pos_2_float
        print("postion x1 and x2:", self.x_1, self.x_2)
        print("speed1, speed2:", self.speed_1, self.speed_2)

    def setPosition(self):
        # get the position and with get_rect() set the new position
        circle_left.rect.x = self.x_1
        circle_right.rect.x = self.x_2

    def checkCollide(self):
        if self.pos_1_float <= self.wall_1:
            print("collide pos_1_float with wall")
            if self.pos_1_float + self.radius_ball >= self.pos_2_float - self.radius_ball:
                self.calculateSpeedCollision()
                self.calculateSpeedWall('x1')
            else:
                self.calculateSpeedWall('x1')

        if self.pos_1_float + self.radius_ball >= self.pos_2_float - self.radius_ball:
            if self.pos_1_float <= self.wall_1:
                self.calculateSpeedCollision()
                self.calculateSpeedWall(('x1'))
            else:
                print("collision balls")
                self.calculateSpeedCollision()


pygame.init()
# generate screen
(width, height) = (800, 450)
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("simulation")
screen.fill(background_colour)

# generate walls
wall_left = Wall()

# generate cirkles on startposition
circle_left = Circle((0, 255, 255))
circle_right = Circle((0, 255, 255))

# lists for Sprites
circles_sprites_list = pygame.sprite.Group()
walls_sprites_list = pygame.sprite.Group()

wall_left.rect.x = float(20)
wall_left.rect.y = float(25)


circle_left.rect.x = float(300)
circle_left.rect.y = float(200)

circle_right.rect.x = float(400)
circle_right.rect.y = float(200)

circle_right.rect.x = float(circle_right.rect.x)

test = circle_right.rect.x


circles_sprites_list.add(circle_left)
circles_sprites_list.add(circle_right)
walls_sprites_list.add(wall_left)


mmf = mathMakesFun()
mmf.radius_ball = 25
mmf.wall_1 = 50

mmf.pos_1_float = 300
mmf.pos_2_float = 400

mmf.speed_1 = 0
mmf.speed_1 = float(mmf.speed_1)
mmf.speed_2 = -2
mmf.speed_2 = float(mmf.speed_2)
mmf.mass_1 = 1
mmf.mass_2 = 10
mmf.counter_collision = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    mmf.checkCollide()
    mmf.calculatePosition()
    mmf.setPosition()

    walls_sprites_list.draw(screen)
    circles_sprites_list.draw(screen)

    pygame.display.update()
    pygame.display.flip()
