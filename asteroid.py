import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


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
        
        rAngle = random.uniform(20, 50)

        vect1 = self.velocity.rotate(rAngle)
        vect2 = self.velocity.rotate(-rAngle)
        radii = self.radius - ASTEROID_MIN_RADIUS
        
        ast1 = Asteroid(self.position.x, self.position.y, radii)
        ast2 = Asteroid(self.position.x, self.position.y, radii)

        ast1.velocity = vect1 * 1.2
        ast2.velocity = vect2 * 1.2