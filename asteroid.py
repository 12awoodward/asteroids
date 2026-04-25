import pygame
import random

# classes from files
from logger import log_event
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        # remove old asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # random value
        direction_diff = random.uniform(20, 50)
        # +/- random value for angles
        directions = [
            self.velocity.rotate(direction_diff),
            self.velocity.rotate(-direction_diff),
        ]
        # smaller radius
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        # create and speed up new asteroids
        for direction in directions:
            new_ast = Asteroid(self.position[0], self.position[1], new_rad)
            new_ast.velocity = direction * 1.2
