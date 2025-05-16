import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

 
    while True:
        # allows for when 'x' is pressed to exit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)

        for object in updateable:
            object.update(dt)

                

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.split()
                    shot.kill()


        dt = clock.tick(60) / 1000


        

if __name__ == "__main__":
    main()

