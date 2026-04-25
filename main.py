import pygame

# Classes from files
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(pygame.init())
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # setup clock for timing
    clock = pygame.time.Clock()
    # delta time
    dt: float = 0
    # score
    score = 0
    score_timer = 0

    # create object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # fill object groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    # player at center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # asteroid spawner
    _ = AsteroidField()

    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"\nSCORE: {score}")
                return

        updatable.update(dt)

        # asteroid collisions
        for asteroid in asteroids:
            if isinstance(asteroid, Asteroid):
                # with player
                if asteroid.is_colliding(player):
                    log_event("player_hit")
                    print("Game over!")
                    print(f"\nSCORE: {score}")
                    exit()

                # with bullets
                for shot in shots:
                    if isinstance(shot, Shot):
                        if shot.is_colliding(asteroid):
                            log_event("asteroid_shot")
                            shot.kill()
                            asteroid.split()
                            break

        # draw bg
        screen.fill("black")

        for item in drawable:
            if isinstance(item, CircleShape):
                item.draw(screen)

        # show frame
        pygame.display.flip()

        # delta time - ms to s + limit to 60fps
        dt = clock.tick(60) / 1000
        score_timer += dt

        # increment score every second
        if score_timer >= 1:
            score_timer = 0
            score += 1


if __name__ == "__main__":
    main()

