import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def get_position(self):
        return self.position
    
    def get_radius(self):
        return self.radius

    def collide(self, other_circle):
        radius_total = self.get_radius() + other_circle.get_radius()
        if self.get_position().distance_to(other_circle.get_position()) <= radius_total:
            return True
        else:
            return False

