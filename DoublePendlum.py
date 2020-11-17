import pygame
import math


class makeBalls:
    def __init__(self):
        colour = (0, 0, 0)
        super().__init__()

        pygame.draw.circle(screen, colour, mmm.pos_fixed, 10)

    def makeBallOne(self, screen, pos):
        colour = (0, 0, 0)
        super().__init__()

        pygame.draw.circle(screen, colour, pos, 10)

    def makeBallTwo(self, screen, pos):
        colour = (0, 0, 0)
        super().__init__()

        pygame.draw.circle(screen, colour, pos, 10)

    def drawLines(self):
        pygame.draw.line(screen, (0, 0, 0), mmm.pos_1, mmm.pos_2, 2)
        pygame.draw.line(screen, (0, 0, 0), mmm.pos_1, mmm.pos_fixed, 2)


class MathMathMath:

    def calculateAngleOne(self):
        num1 = -self.g*(2*self.m1+self.m2)*math.sin(self.a1)
        num2 = self.m2*self.g*math.sin(self.a1-2*self.a2)
        num3 = 2*math.sin(self.a1-self.a2)*self.m2
        num4 = (self.a2_v**self.a2_v)*self.radius_line
        c = complex(num4)
        num5 = (self.a1_v**self.a1_v)*self.radius_line*math.cos(self.a1-self.a2)
        c = complex(num5)
        numS = num4 + num5
        c = complex(numS)
        num6 = self.radius_line*(2*self.m1+self.m2-self.m2*math.cos(2*self.a1-2*self.a2))
        com1 = num1 - num2 - (num3 * numS)
        c = complex(com1)
        numSum = c.real
        c = complex(num6)
        n5 = c.real
        self.a1_a = (numSum / n5)
        print("a1_a: {}".format(self.a1_a))

    def calculateAngleTwo(self):
        num1 = 2*math.sin(self.a1-self.a2)
        num2 = (self.a1**self.a1)*self.radius_line*(self.m1+self.m2)
        num3 = self.g*(self.m1+self.m2)*math.cos(self.a1)
        numS = (self.a2**self.a2)*self.radius_line*self.m2*math.cos(self.a1-self.a2)
        result1 = num2+num3+numS
        result2 = num1*result1
        res1 = complex(result2)
        resultR = res1.real
        numDivide = self.radius_line*(2*self.m1+self.m2-self.m2*math.cos(2*self.a1-2*self.a2))
        cd = complex(numDivide)
        nD = cd.real
        self.a2_a = (resultR/nD)
        print("a2_a: {}".format(self.a2_a))

    def calculatePosition(self):
        self.calculateAngleOne()
        self.calculateAngleTwo()
        print("test test: {}".format(self.a1_a))
        print(type(self.a1_a))
        print("debug type: {}".format(type(self.a2_a)))
        self.a1_v += self.a1_a
        self.a2_v += self.a2_a
        self.a1 += self.a1_v
        self.a2 += self.a2_v
        self.a1_v = 0
        self.a2_v = 0
        print("a1: {}".format(self.a1))
        print("a2: {}".format(self.a2))
        self.x1 = self.x_fixed+math.sin(self.a1)*self.radius_line
        self.y1 = self.y_fixed+math.cos(self.a1)*self.radius_line
        self.x2 = self.x1+math.sin(self.a2)*self.radius_line
        self.y2 = self.y1+math.cos(self.a2)*self.radius_line
        print("x1: {}".format(self.x1))
        print("x2: {}".format(self.x2))
        self.pos_1 = (self.x1, self.y1)
        self.pos_2 = (self.x2, self.y2)

    def startValues(self):
        self.x_fixed = width/2
        self.y_fixed = height/2
        self.pos_fixed = (self.x_fixed, self.y_fixed)
        self.a1 = math.pi / 4
        self.a2 = math.pi / 8
        self.a1 = float(self.a1)
        self.a2 = float(self.a2)
        self.a1_v = 0
        self.a2_v = 0
        self.a1_v = float(self.a1_v)
        self.a2_v = float(self.a2_v)
        self.radius_line = 50
        self.x1_start = 275
        self.y1_start = height / 2 + self.radius_line
        self.x2_start = 275
        self.y2_start = height / 2 + 2 * self.radius_line
        self.g = 9.81
        self.m1 = 1
        self.m2 = 1
        self.x1 = self.x_fixed+math.sin(self.a1)*self.radius_line
        self.y1 = self.y_fixed+math.cos(self.a1)*self.radius_line
        self.x1 = float(self.x1)
        self.y1 = float(self.y1)
        self.x2 = self.x1+math.sin(self.a2)*self.radius_line
        self.y2 = self.y1+math.cos(self.a2)*self.radius_line
        self.x2 = float(self.x2)
        self.y2 = float(self.y2)
        self.pos_1 = (self.x1, self.y1)
        self.pos_2 = (self.x2, self.y2)


pygame.init()

# generate screen
(width, height) = (550, 600)
background_colour = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("simulation")
screen.fill(background_colour)


mmm = MathMathMath()
mmm.startValues()
print("debug fixed pos: {}".format(mmm.pos_fixed))
mb = makeBalls()
mb.makeBallOne(screen, mmm.pos_1)
mb.makeBallTwo(screen, mmm.pos_2)
mb.drawLines()


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    mmm.calculatePosition()

    mb = makeBalls()
    mb.makeBallOne(screen, mmm.pos_1)
    mb.makeBallTwo(screen, mmm.pos_2)
    mb.drawLines()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(11)
