import pygame
import os

class Background:
    image = pygame.image.load(os.path.join("assets/background", "run.png"))
    #PANNING_VELOCITY = 100

    def __init__(self, width, height, PANNING_VEL):
        self.pan_vel = PANNING_VEL
        self.width = width
        self.height = height
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.x_offset = 0

    def update(self, dt):
        self.x_offset = (self.x_offset - self.pan_vel * dt) % self.image_width

    def draw(self, screen):
        screen.blit(self.image, (self.x_offset, 0))
        screen.blit(self.image, (self.x_offset - self.image_width, 0))