from __future__ import annotations
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius = radius

    # circle -> circle collision
    def is_colliding(self, other_circle: CircleShape):
        return (
            self.position.distance_to(other_circle.position)
            <= self.radius + other_circle.radius
        )

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass
