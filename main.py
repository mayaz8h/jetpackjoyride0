import pygame
from classes.background import Background
from classes.bird import Bird
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEAT - Flappy Bird")

def main():
    run = True
    clock = pygame.time.Clock()

    # Initialize a background
    bg = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

    Bird.birds = [Bird(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "yellow")]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in Bird.birds:
                        bird.jump()

        dt = 1 / 60
        SCREEN.fill((255, 255, 255))

        # Update and draw the background
        bg.update(dt)
        bg.draw(SCREEN)

        # Update and draw the birds
        for bird in Bird.birds:
            bird.update(dt)
            bird.draw(SCREEN)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()