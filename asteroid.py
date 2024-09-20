import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        exit_angle = random.uniform(20, 50)
        split_direction1 = self.velocity.rotate(exit_angle)
        split_direction2 = self.velocity.rotate(-exit_angle)
        new_asteroid_radii = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radii)
        new_asteroid.velocity = split_direction1 * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radii)
        new_asteroid.velocity = split_direction2
