import pygame
import os

pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg_w, bg_h = size 
bg = pygame.image.load(os.path.join("assets/background", "Background.png"))
bg_w = 255
bg_h = 362

pos_x = 0
speed = 10

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    allKeys = pygame.key.get_pressed()
    pos_x += speed if allKeys[pygame.K_LEFT] else -speed if allKeys[pygame.K_RIGHT] else 0

    x_rel = pos_x % bg_w
    x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w

    screen.blit(bg, (x_rel, 0))
    screen.blit(bg, (x_part2, 0))