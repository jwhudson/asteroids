import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()


    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (updateable_group, drawable_group, asteroid_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (updateable_group, drawable_group)

    player = Player(PLAYER_START_X, PLAYER_START_Y)
    asteroid_field = AsteroidField()

    
    dt = 0
 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        for item in updateable_group:
            item.update(dt)


        for asteroid in asteroid_group:
            if asteroid.collide(player):
                print("Game Over!")
                return

        for item in drawable_group:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
