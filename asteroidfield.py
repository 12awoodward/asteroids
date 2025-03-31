import pygame
import random
# classes from files
from asteroid import *
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    # [for each edge: [direction vector, lambda func (pass 0-1 as %, returns position along that edge - offset by max asteroid size)]  ]
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # get random edge
            edge = random.choice(self.edges)
            # get random velocity away from edge
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            # get random angle
            velocity = velocity.rotate(random.randint(-30, 30))
            # gen random position along edge
            position = edge[1](random.uniform(0, 1))
            # pick random size
            kind = random.randint(1, ASTEROID_KINDS)
            # spawn asteroid
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)