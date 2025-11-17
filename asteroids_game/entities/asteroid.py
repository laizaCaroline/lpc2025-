import random
import pygame as pg
import config as C
import math

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, C.WIDTH)
        self.y = random.randint(0, C.HEIGHT)
        self.vx = random.uniform(-80, 80)
        self.vy = random.uniform(-80, 80)
        self.radius = random.randint(20, 40)
        self.alive = True

    def update(self, dt):
        self.x = (self.x + self.vx * dt) % C.WIDTH
        self.y = (self.y + self.vy * dt) % C.HEIGHT

    def draw(self, screen):
        pg.draw.circle(screen, C.WHITE, (int(self.x), int(self.y)), self.radius, 2)

    def collides(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 < (self.radius)**2
