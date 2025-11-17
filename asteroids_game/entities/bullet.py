import pygame as pg
import config as C

class Bullet:
    def __init__(self, x, y, vx, vy, owner):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.owner = owner
        self.radius = 3
        self.life = 3.0

    def update(self, dt):
        self.x = (self.x + self.vx * dt)
        self.y = (self.y + self.vy * dt)
        self.x %= C.WIDTH
        self.y %= C.HEIGHT
        self.life -= dt

    def draw(self, screen):
        color = C.WHITE if self.owner == "player" else C.RED
        pg.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
