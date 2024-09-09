# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pygame.time.Clock()
	dt=0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for to_update in updatable:
			to_update.update(dt)
		for asteroid in asteroids:
			if asteroid.collision_check(player):
				print("Game over!")
				return
			for bullet in shots:
				if asteroid.collision_check(bullet):
					asteroid.split()
					bullet.kill()

		screen.fill("black")

		for to_draw in drawable:
			to_draw.draw(screen)
		
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()

