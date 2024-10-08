import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    asteroidField = AsteroidField()

    Shot.containers = (shots, updateable, drawable)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for object in updateable:
            object.update(dt)
        
        for ast in asteroids:
            if ast.checkForCollision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if ast.checkForCollision(shot):
                    ast.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
