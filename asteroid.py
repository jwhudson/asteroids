from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    

    def split(self):
        self.kill()
        if self.get_radius() > ASTEROID_MIN_RADIUS:
            first_angle = random.uniform(20, 50)
            second_angle = first_angle * -1
            first_velocity = self.velocity.rotate(first_angle)
            second_velocity = self.velocity.rotate(second_angle)

            radius = self.get_radius() - ASTEROID_MIN_RADIUS
            
            first_split_asteroid = Asteroid(self.position.x, self.position.y, radius)
            first_split_asteroid.velocity = first_velocity * 1.2
            second_split_asteroid = Asteroid(self.position.x, self.position.y, radius)
            second_split_asteroid.velocity = second_velocity * 1.2
        