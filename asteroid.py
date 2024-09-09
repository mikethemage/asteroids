import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20,50)           
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.__spawn_new(random_angle, new_radius)
            self.__spawn_new(-random_angle, new_radius)

    def __spawn_new(self, new_angle, new_radius):
        new_vector = self.velocity.rotate(new_angle)
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = new_vector * 1.2

