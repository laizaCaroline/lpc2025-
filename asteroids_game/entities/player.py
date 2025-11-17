import pygame as pg
import math
import random
import config as C

class Player:
    SPEED = 200
    ROT = 180  # degrees per second

    def __init__(self):
        self.x = C.WIDTH // 2
        self.y = C.HEIGHT // 2
        self.angle = 0  # degrees
        self.dirx = 1
        self.diry = 0

    def random_position(self):
        self.x = random.randint(0, C.WIDTH)
        self.y = random.randint(0, C.HEIGHT)

    def update(self, dt, keys):
        if keys[pg.K_LEFT]:
            self.angle -= self.ROT * dt
        if keys[pg.K_RIGHT]:
            self.angle += self.ROT * dt

        rad = math.radians(self.angle)
        self.dirx = math.cos(rad)
        self.diry = math.sin(rad)

        if keys[pg.K_UP]:
            self.x += self.dirx * self.SPEED * dt
            self.y += self.diry * self.SPEED * dt

        self.x %= C.WIDTH
        self.y %= C.HEIGHT

    def draw(self, screen):
        import math
        p1 = (self.x + math.cos(math.radians(self.angle)) * 15,
              self.y + math.sin(math.radians(self.angle)) * 15)
        p2 = (self.x + math.cos(math.radians(self.angle+140)) * 12,
              self.y + math.sin(math.radians(self.angle+140)) * 12)
        p3 = (self.x + math.cos(math.radians(self.angle-140)) * 12,
              self.y + math.sin(math.radians(self.angle-140)) * 12)
        pg.draw.polygon(screen, C.WHITE, [p1, p2, p3])
