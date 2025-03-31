import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  print(pygame.init())
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  score = 0
  score_timer = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable, shots)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print(f"\nSCORE: {score}")
        return
      
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        print("Game over!")
        print(f"\nSCORE: {score}")
        exit()
      
      for shot in shots:
        if shot.is_colliding(asteroid):
          shot.kill()
          asteroid.split()
          break
      
    screen.fill("black")

    for item in drawable:
      item.draw(screen)

    pygame.display.flip()

    # delta time - ms to s + limit to 60fps
    dt = clock.tick(60) / 1000 
    score_timer += dt
    
    if score_timer >= 1:
      score_timer = 0
      score += 1

if __name__ == "__main__":
  main()