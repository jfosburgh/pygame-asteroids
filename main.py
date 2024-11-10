import pygame

from asteroidfields import AsteroidField
from asteroids import Asteroid
from constants import *
from player import Player
from shots import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable, drawable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = (updateable)

    player = Player(
            SCREEN_WIDTH/2,
            SCREEN_HEIGHT/2
    )

    AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))

        for sprite in updateable:
            sprite.update(dt)
            
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game Over!")
                return

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

        pygame.display.flip()

        dt = clock.tick(60)/1000.


if __name__ == "__main__":
    main()
